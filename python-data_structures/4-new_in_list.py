#!/usr/bin/python3
def new_in_list(my_list, x, element):
	if my_list:
		new_list = my_list.copy()
	if x < 0:
		return new_list
	elif x > len(my_list) - 1:
		return new_list
	else:
		new_list[x] = element
		return new_list

