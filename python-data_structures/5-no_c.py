#!/usr/bin/python3
def no_c(my_string):
	solution = ""

	for char in my_string:
		if char != 'c' and char != 'C':
			solution += char

	return solution
