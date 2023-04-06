#!/usr/bin/python3

'''
Implemantation of a Square class
'''


class Square:
    '''
    the class implementation
    '''

    def __init__(self, size=0):
        '''
        Args:
            size: Private instance attr
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
