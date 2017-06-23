from turtle import *
turt = Turtle()

class Polygon(object):
	"""
	Wrapper class for polygons.
	"""
	def __init__(self, tuples, width=None, height=None, top = None):
		self.vertices = [*tuples]
		self.width = width
		self.height = height
		self.top = top
		if not self.width:
			left = self.vertices[0][0]
			right = self.vertices[0][0]
			for i in range(1, len(self.vertices)):
				if self.vertices[i] != "up" and self.vertices[i][0] < left:
					left = self.vertices[i][0]
				elif self.vertices[i] != "up" and self.vertices[i][0] > right:
					right = self.vertices[i][0]
			self.width =  int(right - left)
		if not self.height:
			up = self.vertices[0][1]
			down = self.vertices[0][1]
			self.top = self.vertices[0]
			for i in range(1, len(self.vertices)):
				if self.vertices[i] != "up" and self.vertices[i][1] < down:
					down = self.vertices[i][1]
				elif self.vertices[i] != "up" and self.vertices[i][1] > up:
					up = self.vertices[i][1]
					self.top = self.vertices[i]
			self.height = int(up - down)

	def __len__(self):
		return len(self.vertices)

	def __iter__(self):
		return iter(self.vertices)

	def __getitem__(self, i):
		return self.vertices[i]

	def __repr__(self):
		return repr(self.vertices)

	def shift(self, amount):
		"""
		Non-destructively shifts a polygon by a Vec2D.

		Args:
			poly: Polygon to be shifted, a tuple of Vec2Ds
			amount: vector to shift by, Vec2D

		Returns:
			a new Polygon shifted by amount
		"""
		return Polygon(("up" if self[i] == "up" else (self[i] + amount) for i in range(len(self))), self.width, self.height, self.top + amount)

def poly_compose(base, layer):
	def compose(n):
		poly = None
		if n == 0:
			return base
		elif n == 1:
			poly = base
		else:
			poly = compose(n - 1)
		poly.shift(-poly[0])
		polys = layer(poly)

		temp = [["up"] if i % 2 == 1 else polys[int(i / 2)] for i in range(2 * len(polys) - 1)]
		points = []
		for i in range(len(temp)):
			points += temp[i]
		return Polygon(points)
	return compose

def reg_polygon(n):
	"""
	Traces a regular polygon with n sides and each side having
	unit width without drawing it and returns the polygon created.
	
	Args:
		n: number of sides on regular polygon
	
	Returns:
		a tuple of tuples representing vertex points on the polygon
	"""
	turt.hideturtle()
	turt.speed("fastest")
	turt.penup()
	turt.begin_poly()
	for i in range(n):
		turt.fd(1)
		turt.lt(360 / n)
	turt.end_poly()
	poly = turt.get_poly()
	turt.pendown()
	turt.speed("normal")
	return Polygon(poly)

def sequence(num_sides, relation, side_relation):
	def sequence_compose(depth):
		def side(n):
			if n == 0:
				return '0'
			else:
				s_n = side(n - 1)
				return relation(s_n)
		return num_sides * side_relation(side(depth))
	return sequence_compose

def draw(design_lib, depth, speed):
	"""
	Draws the intended design with attribute dictionary given
	by design_lib. The drawing is a design with specified recursive
	depth and will be drawn at specified speed. If the design is
	formed by recursively drawing polygons, it will get the locations
	of all vertices and connecting lines then draw those. Otherwise,
	the design will be a continuous line which follows a series of
	forward motions and left/right turns, eventually ending back at
	the original start-of-drawing location.

	Args:
		design_lib: dictionary of important attributes and functions,
			which mostly are dependent on the recursive depth, that
			define this design
		depth: the recursive depth of this drawing
		speed: speed at which to construct this design
	"""
	turt.hideturtle()
	turt.speed(speed)
	if design_lib["pattern"] == "polygon":
		poly = design_lib["recurse_func"](depth)
		turt.penup()
		turt.setpos(*poly[0])
		turt.pendown()
		lst = list(range(1, len(poly)))
		for i in lst:
			if poly[i] != "up":
				turt.goto(*poly[i])
			else:
				turt.penup()
				turt.setpos(*poly[i + 1])
				turt.pendown()
	elif design_lib["pattern"] == "sequence":
		seq = design_lib["recurse_func"](depth)
		for elem in seq:
			design_lib["lib"][elem](turt)
	else:
		pass

def layer(n, coords):
	"""
	Produces a function which will return the coordinates of many of the same
	designated polygons at different specified locations. Ex: We want three
	triangle-like polygons to form a triforce; this function produces which
	will know to make 3 new versions (constructively) of the base polygon at
	specified locations to make a triforce of the three triangle-like polygons.

	Args:
		n: number of copies to make; somewhat redundant but good for clarity
		coords: list of Vec2D pairs for the start-of-drawing coordinates for
			each new polygon copy; NOTE: Vec2D's are subclasses of tuples, for
			example v = Vec2D(0, 0) represents the origin. Vec2D objects can
			perform basic vector operations between Vec2Ds.
			# precondition: the first polygon in the list of copies must have
			its tuple pair location as (0, 0)

	Returns:
		a function which will compose the supplied polygon into copies and new
		coordinates as specified
	"""
	def layer_compose(poly):
		"""
		Takes a base polygon and makes n copies of it and returns these copies
		as a list once each copy has been shifted to its proper location

		Args:
			poly: an instance of the Polygon class, polygon to be duplicated;
				look at documenation of Polygon for further info how to use it!

		Returns:
			a list of lists, each representing a duplication of the base polygon,
			with each list item containing the proper coordinates of this polygon
			once it has been shifted
		"""
		return [poly.shift(coords[i](poly)) for i in range(n)]
	return layer_compose
