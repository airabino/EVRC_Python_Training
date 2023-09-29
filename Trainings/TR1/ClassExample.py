'''
This module holds a script which prints out numbers between 1 and 10 and their factorials.
In this module the code block which computes the factorial and prints is an attribute
of the class Factorial as are the constants low and high

The class Factorial inherits from the default meta-class and then two methods are
over-written: __init__() which builds the object and __call__() which provides outputs
when the object is called like a function
'''

'''
Class definition starts with the keyword class
The syntax for class is:

class <class handle>(<super-class>)
if no super-class is entered then the default meta-class is used
'''
class Factorial():

	'''
	Over-writing default __init__
	Note that default values are provided for both arguments
	'''
	def __init__(self, low=1, high=10):
		self.low = low
		self.high = high

	#Over-writing default __call__
	def __call__(self, low=None, high=None):
		
		#Only update low and high if inputted
		if (low is not None) and (high is not None):
			self.__init__(low, high)

		self.Compute()

	def Compute(self):
			num = [i for i in range(self.low, self.high)]

			factorial=num[0]

			for n in num:

				factorial *= n

				print(f'n={n}, n!={factorial}')

'''
This class behaves like a function in that it will be called upon creation. This is
accomplished by having __init__() call __call__()
'''
class FactorialFunction():

	#Over-writing default __init__
	def __init__(self, low, high):
		self.__call__(low, high)

	#Over-writing default __call__
	def __call__(self, low, high):
		self.low = low
		self.high = high
		self.Compute()

	def Compute(self):
			num = [i for i in range(self.low, self.high)]

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