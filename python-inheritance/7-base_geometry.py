#!/usr/bin/python3
""" A class that raises an exception """

class BaseGeometry:
	""" A class that raises an exception """
	def area(self):
	raise Exception("area() is not implemented") #Exception message

	def integer_validator(self, name, value):
		""" Checks if input value is a positive integer """
		if type(value) is not int:
			raise TypeError("{} must be an integer".format(name)) #checks if int
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name)) #checks if above 0 (positive)
