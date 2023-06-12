#!/usr/bin/node

/**
 * Print a message depending on no of arguments
 * If no args, print 'No argument'
 * If only 1 args, print, 'Argument found'
 * If more than 1 args, print, 'Arguments found'
*/

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
