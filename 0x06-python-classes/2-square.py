#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
       if size.isdigit():
           self.__size = size
       else:
           TypeError "size must be an integer"
       if size < 0
           ValueError "size must be >= 0" 
