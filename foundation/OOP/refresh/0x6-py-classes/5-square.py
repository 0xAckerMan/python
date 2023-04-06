#!/usr/bin/python3
'''
class square
'''
import sys


class Square:
    '''
    Implementation of the class
    '''

    def __init__(self, size=0):
        '''
        args: 
            self - private instance attr
        '''

        self.__size = size

    @ property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        '''
        sets the private instance attr size
        '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            sys.stdout.write("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
