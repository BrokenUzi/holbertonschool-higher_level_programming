#!/usr/bin/python3
def lookup(obj):
	""" Returns a list of available attributes """

	""" Gets list of methods using dir() """
	all_attributes_and_methods = dir(obj)

	""" Filters out callable methods """
	attributes = [item for item in all_attributes_and_methods if not callable(getattr(obj, item))]

	return attributes

class Object:
	def __init__(self):
		self.attribute1 = 42

obj = Object()

attributes_and_methods = lookup(obj)
print(attributes_and_methods)
