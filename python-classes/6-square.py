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

	@property
	def position(self):
		return self.__position

	@position.setter
	def position(self, value):
		if not isinstance(value, tuple) or len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")
		if not all(isinstance(item, int) for item in value):
			raise TypeError("position must be a tuple of 2 positive integers")
		if not all(item >= 0 for item in value):
			raise TypeError("position must be a tuple of 2 positive integers")
		else:
			self.__position = value

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
