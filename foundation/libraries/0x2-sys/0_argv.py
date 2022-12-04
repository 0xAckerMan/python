#!/usr/bin/python3

'''
Author: @K0r3s

The argv functions from sys that allows
users to pass arguments to the program
'''

import sys

if len(sys.argv)>2:
	print("Too many arguments passed")
elif len(sys.argv) < 2:
	print('few arguments passed')
else:
	print("Whats your first name: ", sys.argv[1])


