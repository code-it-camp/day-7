from re import match
import unittest, os

def test_case(module, question, question_inputs):
	"""
	Determines if grader has been given a valid question test
	request. Passes important attributes of our TestCase to
	the test_case_factory for our desired TestCase.

	Args:
		module: module containing functions to be tested
		question: user's requested question test (string)
		question_inputs: all question function test inputs
			and expected results

	Returns:
		the desired TestCase for this question
	"""
	# ensures that question is formated as
	# 'q#' with # > 0
	try:
		assert match(r'q[1-9][0-9]*', question)
		assert question in question_inputs
	except:
		print("That is not a question in the file being tested.")
		print("Make sure you're inputting your question in the")
		print("specified form as per the README.md file.")
		return

	# Defines the q#Test class with all the function tests dynamically
	# added to the definition of the class

	return test_case_factory(question + 'Test', module, question_inputs[question])

def test_case_factory(name, module, func_inputs):
	"""
	Produces a subclass of unittest.TestCase with test
	functions for all the functions we want to test from
	module specified in func_inputs (i.e. all functions
	in this specified question) dynamically added.

	Args:
		name: name of the class; format: q#Test
		module: module which contains the functions to be tested
		func_inputs: all test inputs for each function to be
			tested and the expeceted outputs for each test input

	Returns:
		a subclass of unittest.TestCase
	"""
	dic = {}

	# Formatting for printing out question name
	# and ordering to determine which function the
	# question name should be printed before
	q_string = "---------" + len(name[1:name.index('T')]) * "-" + "\nQuestion " + name[1:name.index('T')]
	print_q_string = False
	sorted_keys = list(func_inputs.keys())
	sorted_keys.sort()

	for func in func_inputs:
		# If function's name is alphabetically first,
		# this will be the function before which
		# the formatted Question name is printed.
		# Why alphabetical? unittest.main runs tests
		# functions from TestCase subclasses in
		# alphabetical order.
		if func == sorted_keys[0]:
			print_q_string = True
		
		dic["test_" + func] = test_compose(module, func, func_inputs[func], q_string, print_q_string)
		print_q_string = False

	newclass = type(name, (unittest.TestCase,), dic)
	return newclass

def test_compose(module, func, inputs, q_string, print_q_string):
	"""
	Produces a test function to be added to a
	unittest.TestCase class which will call test
	on the desired function found by name and the
	inputs provided. Why test_compose? Unittest
	only recognizes functions with the format
	test_****(self), thus we have to return a one
	argument class with our function and inputs
	predefined.
	
	Args:
		module: module that contains func
		func: name of function to be tested
		inputs: arguments to be tested in the
			provided function and their expected
			results
		q_string: nice formatted string that
			represents the question to which this
			function belongs
		print_q_string: should only be True for
			one function in each question so that
			we only print once to which question
			following functions belong
	
	Returns:
		a function to be dynamically added to the
		TestCase clas as a test function for a
		specific function in the specified module
	"""
	def test_run(self):
		test(getattr(module, func), inputs, q_string, print_q_string)
	return test_run

def test(func, inputs, q_string, print_q_string):
	"""
	Calculates the received outputs for all tests of the
	designated function and forms a list of received
	outputs, expected outputs, and args passed into the
	function. Passes this into run_tests for testing
	equality among received vs. expected outputs and
	display of results of tests.

	Args:
		func: function being tested
		inputs: list with each item containing args to be
			passed into function and the expected output
			from each function call with those args
		q_string: nice formatted string that
			represents the question to which this
			function belongs
		print_q_string: should only be True for
			one function in each question so that
			we only print once to which question
			following functions belong
	"""
	if print_q_string:
		print(q_string)

	error_occured = False
	try:
		tests = [(func(*inp[0]), inp[1], inp[0]) for inp in inputs]
	except Exception as err:
		print(func.__name__+ ':')
		error_occured = True

		tb_0 = err.__traceback__
		while tb_0.tb_next:
			tb_0 = tb_0.tb_next

		errname = repr(err)[:repr(err).index('(')]
		fname = os.path.split(tb_0.tb_frame.f_code.co_filename)[1]
		lineno = tb_0.tb_lineno
		src = ""

		with open(fname) as fp:
			for i, line in enumerate(fp):
				if i == lineno - 1:
					src = line.strip()

		raw_print = errname + " @ " + fname + " " + str(lineno) + ": " + str(err)
		print(git_bash_format(raw_print, '', 0))
		print(git_bash_format(src, ' ', 4))
		print('--> 0 tests run')
		print()


	if not error_occured:
		run_tests(func.__name__, tests)

def run_tests(test_name, tests):
	"""
	Goes through the received outputs and expected outputs
	of the function being tested and asserts if they are
	equal. Prints if a received output differs from the
	expected output. Prints how many tests were passed for
	this function.

	Args:
		test_name: name of the function being tested; used
			for printing purposes
		tests: list of tuples containing received output,
			expected output, and args passed into the
			function; each list item represents one test
			of the function
	"""
	tests_passed = 0
	print(test_name + ":")
	for test in tests:
		try:
			assert test[0] == test[1]
			tests_passed += 1
		except:
			raw_print = "Arguments: " + str(test[2]) + " Expected: " + str(test[1]) + "  Received: " + str(test[0])
			print(git_bash_format(raw_print, ' ', 4))
			break
	print("--> " + str(tests_passed), "out of", min(tests_passed + 1, len(tests)), "tests passed")
	print()

def git_bash_format(string, filler, indent):
	content_width = 80 - indent * len(filler)
	lines = [string[content_width * i: content_width * (i + 1)] for i in range(len(string) // content_width)]
	lines += [string[(len(string) // content_width) * content_width:]]
	formatted_print = filler * indent + ("\n" + filler * indent).join(lines)
	return formatted_print

class q(unittest.TestCase):
	"""
	DO NOT DELETE THIS CLASS
	"""
	pass
