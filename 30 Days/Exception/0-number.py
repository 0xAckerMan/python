#!/usr/bin/python3

'''
Using try and except to cat user input errors
when a user does not enters an int to the program
'''

try:
    x = int(input("Enter x: "))
    print(f"x is {x}")

except ValueError:
    print('x is not an integer')