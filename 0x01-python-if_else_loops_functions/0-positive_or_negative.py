#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
	print("{} is zero".fomart(number))
elif number % 2 == 0:
	print("{} is positive".fomart(number))
else:
	print("{} is negative")
