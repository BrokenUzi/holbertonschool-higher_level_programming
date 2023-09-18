#!/usr/bin/python3
class Square:
	"Square is being represented"

	def __init__(self, size=0):
		"size (int):"
		if not isinstance(size, int):
			"Checks if size value is an int. If its not an int Type Error occurs demainding an int"
			raise TypeError("size must be an integer")
		elif size <= 0:
			"Checks if size int is greater than 0. It'll raise a type error if not > 0"
			raise TypeError("size must be >= 0")
		self._size = size
