#!/usr/bin/node

/**
 * Print the addition of 2 integers
 * First arg = First Integer
 * Second arg = Second Integer
 * Prototype: function add(a, b)
*/

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add (a, b) {
  if (isNaN(num1) || isNaN(num2)) {
    return NaN;
  } else {
    return a + b;
  }
}

console.log(add(num1, num2));
