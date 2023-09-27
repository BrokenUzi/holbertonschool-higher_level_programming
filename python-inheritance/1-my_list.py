#!/usr/bin/python3
""" My list class (Inheretance) """

class Mylist(list):

	""" Inheretance from a list (sorted) """
	def print_sorted(self):
		""" Prints sorted """
		print(sorted(self))
