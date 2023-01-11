#!/usr/bin/python3
"""Contains the Square class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    """
    def __init__(self, size):
        """Instantiates size
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Implements string format
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """implements area
        Return:
            The return. Neatly formated area
        """
        res = self.__size * self.__size
        return res
