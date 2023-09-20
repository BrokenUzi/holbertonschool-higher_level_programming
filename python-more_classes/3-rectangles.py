#!/usr/bin/python3
""" Rectangle class with height and width attributes """


class Rectangle:
	""" The Rectangle class """
	def __init__(self, width=0, height=0):
		""" Initialize height and width """
		self.width = width
		self.height = height

	@property
	def width(self):
		""" returns width of Rectangle """
		return self.__width

	@width.setter
	def width(self, value):
		""" sets width to value and value testing """
		if type(value) is not int:
			raise TypeError("width must be an integer")
		elif value < 0:
			raise ValueError("width must be >= 0")
		else:
			self.__width = value

	@property
	def height(self):
		""" Returns height of Rectangle """
		return self.__height

	@height.setter
	def height(self, value):
		""" sets width to value and value testing """
		if type(value) is not int:
			raise TypeError("height must be an integer")
		elif value < 0:
			raise ValueError("height must be >= 0")
		else:
			self.__height = value

	def area(self):
		""" Initialize Area """
		return self.__width * self.__height

	def perimeter(self):
		""" Initialize Perimeter """
		if self.__width == 0 or self.__height == 0:
			return 0
		return (2 * (self.__width + (2 * self.__height)))

	def __str__(self):
		""" String version of the rectangle """
		if self.__width == 0 or self.__height == 0:
            		return ""
		else:
			rect_str = ""
			for _ in range(self.__height):
				rect_str += "#" * self.__width + "\n"
			return rect_str[:-1]
