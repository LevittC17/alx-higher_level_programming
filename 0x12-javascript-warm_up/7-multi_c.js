#!/usr/bin/node

/**
 * Print x times 'C is fun'
 * Using a While loop
*/

const args = process.argv.slice(2);
const num = parseInt(args[0]);

// check if x is a number
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  // Iterate through num to print 'C is fun'
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
