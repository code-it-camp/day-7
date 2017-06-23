from math import *
from turtle import *
from fractallib import *
screen = Screen()
_speed = "fastest"

design_attrs = {
	"s-t": {
		"name": "Sierpinski Triangle",
		"width": lambda n: 2 ** n,
		"height": lambda n: 3 ** 0.5 * 2 ** (n - 1),
		"start": lambda n: (0, 0),
		"pattern": "polygon",
		"recurse_func": poly_compose(reg_polygon(3),
			layer(3,
				[
					lambda poly: (0, 0),
					lambda poly: (poly.width, 0),
					lambda poly: (poly.top[0], poly.top[1])
				]
			)
		)
	},
	"k-sn": {
		"name": "Koch Snowflake",
		"width": lambda n: 3 ** n,
		"height": lambda n: 2 * 3 ** (n - 0.5),
		"start": lambda n: (0, 3 ** (n + 0.5) / 2),
		"pattern": "sequence",
		"recurse_func": sequence(3, lambda s: s+'1'+s+'2'+s+'1'+s, lambda s: s + '2'),
		"lib": {
			"0": lambda t: t.fd(1),
			"1": lambda t: t.lt(60),
			"2": lambda t: t.rt(120)
		}
	},
	"s-s": {
		"name": "Sierpinski Square",
		"width": lambda n: 3 ** n,
		"height": lambda n: 3 ** n,
		"start": lambda n: (0, 3 ** (n - 2)),
		"pattern": "polygon",
		"recurse_func": poly_compose(reg_polygon(4),
			layer(4,
				[
					lambda poly: (0, 2 * poly.width),
					lambda poly: (2 * poly.width, 2 * poly.width),
					lambda poly: (2 * poly.width, 0),
					lambda poly: (0, 0)
				]
			)
		)
	},
	"k-sq": {
		"name": "Koch Square",
		"width": lambda n: 2 * 3 ** n - 1,
		"height": lambda n: 2 * 3 ** n - 1,
		"start": lambda n: (0.5 * (3 ** n - 1), 0.5 * (3 ** (n + 1) - 1)),
		"pattern": "sequence",
		"recurse_func": sequence(4, lambda s: s+'1'+s+'2'+s+'2'+s+'1'+s, lambda s: s + '2'),
		"lib": {
			"0": lambda t: t.fd(1),
			"1": lambda t: t.lt(90),
			"2": lambda t: t.rt(90)
		}
	},
	"k-p": {
		"name": "Koch Pentagon",
		"width": lambda n: 2 * 3 ** n,
		"height": lambda n: 3 ** (n + 1) * (1 / cos(54) + tan(54)),
		"start": lambda n: (3 ** n / 2, 0),
		"pattern": "sequence",
		"recurse_func": sequence(5, lambda s: s+'1'+s+'2'+s+'2'+s+'2'+s+'1'+s, lambda s: s + '2'),
		"lib": {
			"0": lambda t: t.fd(1),
			"1": lambda t: t.lt(108),
			"2": lambda t: t.rt(72)
		}
	},
	"k-h": {
		"name": "Koch Hexagon",
		"width": lambda n: 2 * 4 ** n,
		"height": lambda n: 3 ** 0.5 * (2 * 3 ** n - 1),
		"start": lambda n: (3 ** n - 1 / 2, 0),
		"pattern": "sequence",
		"recurse_func": sequence(6, lambda s: s+'1'+s+'2'+s+'2'+s+'2'+s+'2'+s+'1'+s, lambda s: s + '2'),
		"lib": {
			"0": lambda t: t.fd(1),
			"1": lambda t: t.rt(120),
			"2": lambda t: t.lt(60)
		}
	}
}

def main():
	first = True
	while first or textinput("New Design?", "Y/N").lower() == 'y':
		design = ' '
		while design not in design_attrs.keys() and design:
			design = textinput("Fractal Design", "Ex: 's-t' for a Sierpinski Triangle")
		depth = numinput(design_attrs[design]["name"], "Recursion Depth:", 2, minval=0)
		design_lib = design_attrs[design]
		width = design_lib["width"](depth)
		height = design_lib["height"](depth)
		start = design_lib["start"](depth)
		screen.reset()
		screen.setworldcoordinates(-width / 3 - start[0], -height / 3 - start[1], 4 * width / 3 - start[0], 4 * height / 3 - start[1])
		draw(design_lib, depth, _speed)
		first = False
	done()

if __name__ == '__main__':
	main()
