#!/usr/bin/node

/**
 * Print the first arguments passed
 * No arguments: If none, print 'No argument'
 * You must use `console.log()` to print all output
 *
*/

const args = process.argv.slice(2);

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
