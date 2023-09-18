#!/usr/bin/python3
""" Defines Square Class with __size """


class Square:
	""" Square is being represented """
	def __init__(self, __size=0):
		""" __size (int): """
		if not isinstance(__size, int):
			"Checks if size value is an int. If its not an int Type Error occurs demainding an int"
			raise TypeError("size must be an integer")
		elif __size < 0:
			"Checks if size int is greater than 0. It'll raise a type error if not > 0"
			raise TypeError("size must be >= 0")
		else:
			self.__size = __size
