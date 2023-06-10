## 0x03. Python - Data Structures: Lists, Tuples

Resources

[3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
[Data structures (*until 5.3. Tuples and Sequences included*)](https://docs.python.org/3/tutorial/datastructures.html)
[Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

Tasks

0. Print a list of integers

* Write a function that prints all integers of a list
	. Prototype:  `def print_list_integer(my_list=[]):`
	. Format: one integer per line
	. You are not allowed to import any module
	. You can assume that the list only contains integers
	. You are not allowed to cast integers to strings
	. Yiu have to use `str.format()` to print integers

The Solution:
	.` def print_list_integer(my_list = []):
	       # Iterate through the list
	       for i in my_list:
                   print("{:d}".format(i))

	   def print_list_integer(my_list = [1, 2, 3, 4, 5])`
 
1. Secire access to an element in a list

* Write a function that retrieves an element from a list like in C
	. Prototype: `def element_at(my_list, idx):`
	. If `idx` is negative, the function should return `None`
	. If `idx` is out of range (>of number of element in `my_list`), the
	  function should return `None`
	. You are not allowed to import any module
	. You are not allowed to use `try/except`
