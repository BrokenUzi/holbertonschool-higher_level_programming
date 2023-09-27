#!/usr/bin/python3
""" Defines a Student """

class Student:
	""" Student Class with first and last name with age attributes """
	pass

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		return self.__dict__
