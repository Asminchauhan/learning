# def statement to make functions 



def asmin():
    print('I am the king of the world')

asmin()

def printwith(word):
    print(word + "!")

printwith("Chauhan")

def print_sum(x, y):
    print(x + y)

print_sum(2,10)

def function(variable):
    variable += 1
    print(variable)

def max(x, y):
    if x >= y:
        return x 
    else:
        return y

print(max(3, 5))
z = max(8,5)
print(z)

"""
This is called Docstrings
"""

# Modules 

import random

for i in range(5):
    value = random.randint(25, 30)
    print(value)


from math import pi, sqrt

print(pi)
print(sqrt(81))

from math import sqrt as square_root

# The last type is called the standard library, and contains many useful modules. 
# Some of the standard library's useful modules include string, re, datetime, 
# math, random, os, multiprocessing, subprocess, socket, email, json, doctest, 
# unittest, pdb, argparse and sys.

