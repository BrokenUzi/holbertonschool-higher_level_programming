#!/usr/bin/python3

class Square:
	"""Defines Square Class with __size"""

	def __init__(self, size=0):
	"""__size (int):"""
	if not isinstance(size, int):
		"""Checks if size value is an int. If it's not an int, a TypeError occurs demanding an int."""
		raise TypeError("size must be an integer")
	elif size < 0:
		"""Checks if size int is greater than 0. It'll raise a type error if not >= 0."""
		raise ValueError("size must be >= 0")
	else:
		self.__size = size

	def area(self):
	"""Returns the current square area."""
		return self.__size ** 2
