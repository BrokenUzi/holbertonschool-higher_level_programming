#!/usr/bin/python3
class Square:
    "Square is being represented"

    def __init__(self, size):
        "size (int):"
        if not isinstance(size, int):
            print("size must be an integer")
        elif size <= 0:
            print("size must be >= 0")
        else:
            self.__size = size

my_square = Square(5)

