#!/usr/bin/node

/**
 * Prints and computes a factorial
 * Must do it recursively
 * Factorial of NaN is 1
*/

const num = parseInt(process.argv[2]);

function factorial (num) {
  // check if not a number
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
