'''
This module shows some features of modules including imports and naming

It is recommended to organize modules in the following order:

1. imports
2. definitions
3. script

The order of imports and definitions does not matter in Python but if a definition
is called in script above the definition the interpreter will throw an exception

'''

'''
imports:

Sometimes one may want to import a whole module in which case the syntax is:

import <module> or import <module> as <handle>

in either case the attributes of the module can be accessed by the handle as with any
other object

It also might be preferable to import a subset of attributes from  module in which the
syntax is:

from <module> import <attribute> as <handle>

at which point the attribute is accessible using the handle
'''
import sys
import FunctionExample
from FunctionExample import Factorial

if __name__ == "__main__":

	'''
	We are going to have the option to take input arguments from the command line
	Command line arguments can be accessed through the sys.argv attribute

	If the command line call is:

	python ModuleExample.py 1 10

	then sys.argv will be:

	['ModuleExample.py','0','10']

	with all inputs being treated as strings
	'''

	argv=sys.argv

	if len(sys.argv) == 3:
		Factorial(int(argv[1]), int(argv[2]))

	else:
		Factorial(1, 8)
		'''
		equivalent to:
		FunctionExample.Factorial(1, 8)
		'''

	print('\nNote that the __name__ for the FunctionExample module'+
		f' is {FunctionExample.__name__}\n'+
		'so the script from the FunctionExample module doesn\'t run.\n'+
		'ModuleExample is now __main__\n')