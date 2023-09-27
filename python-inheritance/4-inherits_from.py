#!/usr/bin/python3
""" Checks if object is inhereted from a class """
def inherits_from(obj, a_class):
	""" Checks if object is inhereted from a class """
	if type(obj) is a_class:
		return False
	else:
		return isinstance(type(obj), a_class)
