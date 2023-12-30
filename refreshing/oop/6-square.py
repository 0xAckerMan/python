#!/usr/bin/python3


class Square:

    def __init__(self, size = 0, position = (0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0 :
            raise ValueError("size must be > 0")
        self.__size = size

    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 \
            or not all(isinstance(num, int) for num in value) or \
            not all(num >= 0 for num in value):
            raise TypeError("positon must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        """prints a square  with the corresponding size
        """
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
