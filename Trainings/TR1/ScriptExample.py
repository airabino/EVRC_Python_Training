'''
This module holds a script which prints out numbers between 1 and 10 and their factorials
Calling this function will run the below code top-to-bottom
'''

low = 1
high = 10

num = [i for i in range(low, high)]

factorial=num[0]

for n in num:

	factorial *= n

	print(f'n={n}, n!={factorial}')