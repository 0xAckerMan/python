#!/usr/bin/python3
'''
Defines a class square
'''


class Square:
    '''
    implementation of the class
    '''

    def __init__(self, size=0):
        '''
        Args:
            size - Must be int and >0
        '''

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        self.__size = size

    def area(self):
        '''
        calculates the area of a circle
        '''

        return self.__size ** 2
