#!/usr/bin/python3
#!/usr/bin/python3
""" Define Square Class with __size """


class Square:
	""" Square being represented """
	def __init__(self, size=0):
		""" __size (int): """
		self.__size = size
	@property
	def area(self):
		""" Set's square size """
		return self.__size ** 2

	@size.set
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise TypeError("size must be >= 0")
		self.__size = value

	def area(self):
		""" Area """
		return (self.__size * self.__size)
