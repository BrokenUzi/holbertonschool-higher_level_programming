#!/usr/bin/python3
""" Returns a lost of available attributes and methods """

def lookup(obj):
	""" Gets list of available attributes and methods """
	all_attributes_and_methods = dir(obj)

	""" Filters out callable methods from list """
	attributes = [item for item in all_attributes_and_methods if not callable(getattr(obj, item))]

	return attributes

class Lst:
	def __init__(self):
		self.attribute1 = 42

	def method1(self):
		pass

obj = Lst()

attributes_and_methods = lookup(obj)
print(attributes_and_methods)
