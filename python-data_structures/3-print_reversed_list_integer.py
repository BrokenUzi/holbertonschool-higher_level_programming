#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

	if idx < 0 or idx >= len(my_list):
		return my_list[:]

	new_list = my_list[:]

	new_list[idx] = element

	return new_list
