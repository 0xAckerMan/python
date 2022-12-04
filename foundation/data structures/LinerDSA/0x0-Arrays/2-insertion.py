#/usr/bin/python3

'''
we use .insert to add an elemet at any point of the array 
'''

from array import *

MyArray = array('i',[10,20,30,40,50])

MyArray.insert(1,70)

for _ in MyArray:
	print(_)
