#!/usr/bin/python3
"""Define a class square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialises the data
        Args:
            size (int): The size of the new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
