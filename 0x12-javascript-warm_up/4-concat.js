#!/usr/bin/node

/**
 * Script that prints 2 arguments passed to it
 * Format: "is"
 * Example: ./4-concat.js c cool
 * Output: c is cool
*/

const args = process.argv.slice(2)

if (args.length >= 2) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log('undefined is undefined');
}
