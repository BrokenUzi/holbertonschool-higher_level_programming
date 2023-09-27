#!/usr/bin/python3
""" is_same_class checks if its the same class """

def is_same_class(obj, a_class):
	""" Checks if its the same class """
	return type(obj) is a_class

class C1:
	pass

obj1 = C1()
obj2 = "Yo yo yo"

""" True """
print(is_same_class(obj1, C1))
""" True """
print(is_same_class(obj2, str))
""" False """
print(is_same_class(obj2, int))
