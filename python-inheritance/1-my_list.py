#!/usr/bin/python3
""" My list class (Inheretance) """

class Mylist(list):

	""" Inheretance from a list (sorted) """
	def print_sorted(self):
		""" Prints sorted """
		sorted_list = sorted(self)
		print(sorted_list)
