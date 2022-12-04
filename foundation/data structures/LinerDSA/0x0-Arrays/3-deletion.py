#!/usr/bin/python3

'''
To delete or remove an element in an array, we use 
remove() function
'''

from array import *

MyArray = array('i',[10,20,30,40,50,60])

MyArray.remove(30)

for _ in MyArray:
	print(_)
