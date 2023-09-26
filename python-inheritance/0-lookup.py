#!/usr/bin/python3
def lookup(obj):
	""" Returns a list of available attributes """
	return [item for item in dir(obj) if not callable(getattr(obj, item))]

class Object:
	def __init__(self):
		self.attribute1 = 42

obj = Object()

attributes_and_methods = lookup(obj)
print(attributes_and_methods)
