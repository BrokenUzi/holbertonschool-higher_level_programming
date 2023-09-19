#!/usr/bin/python3
""" Adds Two ints. b is 98 by default if there isnt a second argument """


def add_integer(a, b=98):
	""" Adds two ints. Floats and ints are allowed """
	if type(a) not in [int, float]:
		raise TypeError("a must be an integer")
	if type(b) not in [int, float]:
		raise TypeError("b must be an integer")
	return int(a) + int(b)
