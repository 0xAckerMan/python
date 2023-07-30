#!/usr/bin/env python3
# Base class

class Base:
    '''class initialisation'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor init'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
