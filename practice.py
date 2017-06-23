from math import *
import time

# ------------------------------------------------------------------------- #
#																			#
# Question 1																#
# ------------------------------------------------------------------------- #
def fibonacci(n):
	"""
	Produces the nth Fibonacci number through recursive calls. Our Fibonacci
	sequence will use 0 as its first number and 0 as its index
	i.e. fibonacci(0) == 0

	Args:
		n: nonnegative integer

	Returns:
		positive integer
	"""
	assert isinstance(n, int) and n >= 0

	# base case 1
	if ________:
		return ________
	# base case 2
	elif ________:
		return ________
	# recursive calls
	else:
		return ________ + ________

def fibonacci_2(n):
	"""
	Same as fibonacci, except you are only allowed to use one base case
	to cover the 0 and 1 index values.
	"""
	assert isinstance(n, int) and n >= 0

	# base case
	if ________:
		return ________
	# recursive calls
	else:
		return ________ + ________

def power(x, n):
	"""
	Defines the power function in terms of recursive calls.
	"""
	if n == 0:
		return 1
	elif n == 1:
		return x
	else:
		# x to the power of floor(n / 2)
		floor_half_power = power(x, ________)
		# x to the power of n
		return ________ * ________ power(x, ________)

# ------------------------------------------------------------------------- #
#																			#
# Question 2																#
# ------------------------------------------------------------------------- #
def partitions(n, m):
	"""
	Computes how many unique sequences of positive integers sum up to equal n,
	where the largest number allowed to be used in the sequence is m.
	Several recursive calls in one function frame are required here.
	Example:
		partitions(5, 4) == 6
		1. 1 + 1 + 1 + 1 + 1
		2. 1 + 1 + 1 + 2
		3. 1 + 2 + 2
		4. 1 + 1 + 3
		5. 2 + 3
		6. 1 + 4

	Args:
		n: positive integer
		m: positive integer

	Returns:
		a positive integer
	"""
	if ________:
		return 1
	elif ________ or ________:
		return 0
	else:
		return partitions(________, ________) + partitions(________, ________)

def partitions_memoized(n, m):
	"""
	Computes how many unique sequences of positive integers sum up to equal n,
	where the largest number allowed to be used in the sequence is m.
	Several recursive calls in one function frame are required here. Use the
	dictionary partitions_memo to store the values of partitions(n, m) once
	they are caluculated to speed up your function.
	Example:
		partitions(5, 4) == 6
		1. 1 + 1 + 1 + 1 + 1
		2. 1 + 1 + 1 + 2
		3. 1 + 2 + 2
		4. 1 + 1 + 3
		5. 2 + 3
		6. 1 + 4

	Args:
		n: positive integer
		m: positive integer

	Returns:
		a positive integer
	"""
	# base case 1
	if ________:
		return 1
	# base case 2
	elif ________ or ________:
		return 0
	# recursive calls
	else:
		# memoize
		if n not in ________:
			partitions_memo[n] = {}
		# memoize + recursive calls
		if m not in ________:
			partitions_memo[n][m] = partitions_memoized(________, ________) + partitions_memoized(________, ________)

	return ________

partitions_memo = {}

def partitions_time_test():
	"""
	Tests how long partitions_memoized takes to perform a calculation.

	Returns:
		a string telling whether partitions_memoized performed the test
		fast enough
	"""
	start = int(round(time.time() * 1000))
	a = partitions_memoized(10000, 100)
	end = int(round(time.time() * 1000))
	if a == 22683324467557455025270363928849330511235016373648534420498657018392011562024963097559021800:
		if end - start < 10000:
			return "Memoized partitions function is fast enough!"
		else:
			return "Memoized partitions function is not fast enough."
	else:
		return "Memoized partitions function did not return the correct number."

def pascal_seq(n):
	"""
	Returns the first n numbers in the Pascal Sequence, given by reading
	the Pascal's Triangle from left to right, top to bottom.
	https://en.wikipedia.org/wiki/Pascal%27s_triangle

	Args:
		n: positive integer, number of elements in the
			Pascal Sequence we want. For n == 1, returns [1].

	Returns:
		a list of numbers
	"""
	assert isinstance(n, int) and n > 0

	# base case for layer == 0 i.e. the only number in this layer is 1
	if (n - 1) == ________:
		return [________]
	# recursive call
	else:
		# Provided n, what layer is the number we want in?
		# HINT: Use  a floor function.
		layer = ________

		# Provided with our layer index, what is the n-value
		# of the first number in the layer?
		floor_n = ________

		# Obtain the sequence of all numbers before the layer
		# containing the number we want the sequence to stop at.
		# HINT: Recursive call
		seq_below = ________

		# Construct a list containing all numbers of Pascal's Trinagle
		# in the layer we want our sequence to stop in.
		seq_level = [1] + [________ for i in range(floor_n + 1, floor_n + layer)] + [1]

		# Return the combination of all numbers before this final
		# layer and the numbers in the final layer up until we've
		# hit the nth total number in the Pascal Sequence
		return ________
