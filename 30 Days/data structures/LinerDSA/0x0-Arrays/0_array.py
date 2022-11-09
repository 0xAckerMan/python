#!/usr/bin/python3
# Author: K0r3s

'''
An example of an array in python

Type code		value
b			Reps int of size 1 byte
B			Reps insigned int of size 1 byte
c			Reps char of size 1 byte
i			Reps sign4ed int of size 2 bytes
I			unsigned int 2 bytes
f			floating point size 4 bytes
d			float 8 bytes
'''

from array import *

MyArray = array('i', [5,10,40,60,61,72])

for _ in MyArray:
	print(_)
