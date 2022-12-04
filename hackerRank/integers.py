'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    elif n >= 2 and n<= 5 and n%2 == 0:
        print("Not Weird")
    elif n >= 6 and n <= 20 and n%2 == 0:
        print('Weird')
    elif n > 20 and n <=100:
        print("Not Weird")
    else:
        print("Weird")
