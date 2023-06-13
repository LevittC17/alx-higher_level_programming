#!/usr/bin/node

/**
 * A script that prints a square
 * Use the character 'X' to print the square
 * Kinda like a matrix -> rows vs columns
*/

const args = process.argv.slice(2);
const size = parseInt(args[0]);

// check if size is a number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
