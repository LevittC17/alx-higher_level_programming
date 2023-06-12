## 0x12. JavaScript - Warm up

#### Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:
	. Scripting (same as we did with Python)
	. Web front-end

### Resources
1. [Writing Javascript Code](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
2. [Variables](https://intranet.alxswe.com/rltoken/zgOWmcpVLZFEmFlmuwayyg)
3. [Data Types](https://intranet.alxswe.com/rltoken/VPd6JWaLrwOBzjAeXNAEqg)
4. [Operators](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
5. [Operator Precedence](https://intranet.alxswe.com/rltoken/PHtcJJk30gBNmlFQ9R4RVg)
6. [Controlling Program Flow](https://intranet.alxswe.com/rltoken/tsreKcNh_KmTmLPHsfvJRw)
7. [Functions](https://intranet.alxswe.com/rltoken/e3EfHIxICdIncGBwwIDbXQ)
8. [Objects and Arrays](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
9. [Intrinsic Objects](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
10. [Module Patterns](https://intranet.alxswe.com/rltoken/g-MgvO09Ur02RhM63gVyXw)
11. [var, let and const](https://intranet.alxswe.com/rltoken/gJi61GeJTRX0g-M0Rx-0Iw)
12. [Javascript Tutorial](https://intranet.alxswe.com/rltoken/Y8hkOcy5jO22lQGyF6_NiA)
13. [Modern JS](https://intranet.alxswe.com/rltoken/NZawtiBjWUpiojnrtVywNw)

More Info

Installing Node 14
	`curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -`
	`sudo apt-get install -y nodejs`

Install semi-standard
[Documentation](https://intranet.alxswe.com/rltoken/35q5Pc6A6KWPyd3kGeRQFg)

	`sudo npm install semistandard --global`




###		TASKS

0. FIRST CONSTANT FIRST PRINT

* Write a script that prints “JavaScript is amazing”:

	. You must create a constant variable called `myVar` with the value “JavaScript is amazing”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`



1. 3 LANGUANGES

* Write a script that prints 3 lines:
	. The first line: “C is fun”
	. The second line: “Python is cool”
	. The third line: “JavaScript is amazing”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`


2. ARGUMENTS

* Write a script that prints a message depending of the number of arguments passed:
	. If no arguments are passed to the script, print “No argument”
	. If only one argument is passed to the script, print “Argument found”
	. Otherwise, print “Arguments found”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`

Reference: [Process argv](https://intranet.alxswe.com/rltoken/5kTYi3rxb6KM1_pivm-tXg)


3. VALUE OF MY ARGUMENT

* Write a script that prints the first argument passed to it:
	. If no arguments are passed to the script, print “No argument”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`
	. You are not allowed to use `length`


4. CREATE A SENTENCE

* Write a script that prints two arguments passed to it, in the following format: “ is ”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`


5. AN INTEGER

* Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
	. If the argument can’t be converted to an integer, print “Not a number”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`
	. You are not allowed to use `try/catch`


6. LOOP TO LANGUAGES

* Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop
	. The first line: “C is fun”
	. The second line: “Python is cool”
	. The third line: “JavaScript is amazing”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`
	. You are not allowed to use any `if/else statement`
	. You can use only one `console.log`
	. You must use a loop (`while`, `for`, etc.)


7. I LOVE C

* Write a script that prints `x` times “C is fun”

	. Where `x` is the first argument of the script
	. If the first argument can’t be converted to an integer, print “Missing number of occurrences”
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`
	. You can use only two `console.log`
	. You must use a loop (`while`, `for`, etc.)


8. SQUARE

* Write a script that prints a square
	. The first argument is the size of the square
	. If the first argument can’t be converted to an integer, print “Missing size”
	. You must use the character `X` to print the square
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`
	. You must use a loop (`while`, `for`, etc.)


9. ADD

* Write a script that prints the addition of 2 integers
	. The first argument is the first integer
	. The second argument is the second integer
	. You have to define a function with this prototype: `function add(a, b)`
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`


10. FACTORIAL 

Write a script that computes and prints a factorial

	. The first argument is integer (argument can be cast as integer) used for computing the factorial
	. Factorial of `NaN` is `1`
	. You must do it recursively
	. You must use a function
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`


11. SECOND BIGGEST!

* Write a script that searches the second biggest integer in the list of arguments.
	. You can assume all arguments can be converted to integer
	. If no argument passed, print `0`
	. If the number of arguments is 1, print `0`
	. You must use `console.log(...)` to print all output
	. You are not allowed to use `var`


12. OBJECT

* Update this script to replace the value `12` with `89`:
	. You are not allowed to use `var`

13. ADD FILE

* Write a function that returns the addition of 2 integers.
	. The function must be visible from outside
	. The name of the function must be `add`
	. You are not allowed to use `var`
[Tip](https://intranet.alxswe.com/rltoken/1k6VPdLchwtGubOfPyGL1Q)
