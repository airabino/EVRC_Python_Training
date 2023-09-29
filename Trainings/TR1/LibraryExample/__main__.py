'''
__main__ script for the library
'''

from .Factorial import *

low = 1
high = 10

print('\nCreating the object using __init__() then calling a class method\n')

f = Factorial(low, high)
f.Compute()

'''
equivalent logical cells would be
f = Factorial(low, high).Compute()
f = Factorial(low, high)()
f = Factorial()(low, high)
f = Factorial()()
'''

print('\nCalling __call__() in __init__() like a function\n')

FactorialFunction(low, high)

print('\nThese produce the same output\n')