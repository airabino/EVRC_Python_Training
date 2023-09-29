'''
This module holds a script which prints out numbers between 1 and 10 and their factorials.
In this module the code block which computes the factorial and prints is stored in a function
definition
'''

'''
The def keyword is used to create a function object. One property of a function object is
that it is called upon intialization.
The syntax for def is:

def <function handle>(<args>,<kwargs>)
'''

def Factorial(low, high):
	num = [i for i in range(low, high)]

	factorial=num[0]

	for n in num:

		factorial *= n

		print(f'n={n}, n!={factorial}')

'''
This is the start of the script section of the module
This section of code will only run if this module is called directly and is
designated as __main__
'''
if __name__ == '__main__':
	low = 1
	high = 10

	Factorial(low, high)