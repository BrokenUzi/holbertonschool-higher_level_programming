#!/usr/bin/python3
""" Define Square Class with __size """


class Square:
	""" Square being represented """
	def __init__(self, size=0):
		""" __size (int): """
		if not isinstance(size, int):
			""" Checks if value is an int. If not an int Type Error occurs demanding an int """
			raise TypeError("size must be an integer")
		elif size < 0:
			""" Checks if size int greater than 0. It'll raise a type error if not > 0 """
			raise TypeError("size must be >= 0")
		else:
			self.__size = size

	def area(self):
		return self.__size ** 2
