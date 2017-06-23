import unittest, sys
from graderlib import test_case
import solutions as module

"""
Dictionary of allowed question test requests
	Dictionary of functions in practice part
	of this question test
		Function to be tested: list of lists
		which correspond to a test input for
		this function and an expected output
			Tuple of tuples: each tuple inside
			main tuple represents inputs to
			a call: i.e. first tuple represents
			inputs into actual function, 2nd
			tuple are the inputs passed into
			returned function if one is expected,
			etc. Reflected by change in graderlib
"""
question_inputs = {
	"q1": {
		"fibonacci": [
			[(0,), 0],
			[(1,), 1],
			[(2,), 1],
			[(5,), 5],
			[(10,), 55]
		],
		"fibonacci_2": [
			[(0,), 0],
			[(1,), 1],
			[(2,), 1],
			[(5,), 5],
			[(10,), 55]
		],
		"power": [
			[(2, 4), 16],
			[(4, 7), 16384]
		]
	},
	"q2": {
		"partitions": [
			[(6, 4), 9],
			[(5, 3), 5],
			[(10, 6), 35]
		],
		"partitions_memoized": [
			[(1000, 100), 15658181104580771094597751280645]
		],
		"partitions_time_test": [
			[(), "Memoized partitions function is fast enough!"]
		]
		"pascal_seq": [
			[(1,), [1]],
			[(15,), [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1]]
		]
	}
}

def run_test(questions):
	for question in questions:
		# test is the instance of our TestCase class with all of our
		# desired question, specified by argv[1], functions to be tested.
		test = test_case(module, question, question_inputs)

		# not test corresponds to a requested question test which
		# doesn't exist
		if not test:
			return

		# adds our TestCase to the global attributes so that unittest
		# will find it when it searches for TestCases to run
		globals()[test.__name__] = test

	# Displays which questions are being tested
	plural = ('s ' if len(questions) > 1 else ' ')
	q_string = ', '.join([questions[i][1:] for i in range(len(questions))])
	print('\nRunning Test' + plural + 'for Question' + plural + q_string)
	print()


	"""
	argv='q' allows the program to use the command line arguments
	as the question input. q is a dummy attribute class of __main__
	so that the unittest will run that as the passed in command
	arguments, then our program can access the actual command args
	without them messing up the unittest! DO NOT make the value for
	argv more than one character: no clue why, but the unittest main
	function tries to split the argv value into single characters so
	unless we have each of those individual characters defined as
	dummy attribute classes of __main__ (which there's no reason to
	do so), so leave argv='q'.
	"""
	unittest.main(argv='q')

def main():
	# Test all questions.
	if len(sys.argv) == 1:
		run_test([question for question in question_inputs])
	# Test one specific question specified
	# by the single argument passed in.
	elif len(sys.argv) == 2:
		run_test([sys.argv[1]])
	# Too many arguments.
	else:
		run_test([sys.argv[i] for i in range(1, len(sys.argv))])

if __name__ == '__main__':
	main()
