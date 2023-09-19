#!/usr/bin/python3
""" Define Square Class with __size """


class Square:
	""" Square being represented """
	def __init__(self, size=0):
		""" __size (int): """
		self.__size = size

	@property
	def size(self):
		""" Set's square size """
		return self.__size

	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		""" Area """
		return (self.__size ** 2)

	def my_print(self):
		""" Prints the square """
		if self.__size == 0:
			print()
		for row in range(self.__size):
			for collum in range(self.__size):
				print("#", end="")
			print()
