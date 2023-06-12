#!/usr/bin/node

/**
 * Script that prints My number: <first argument converted in integer>
 * If the first argument can be converted to int
*/

const args = process.argv.slice(2);
const number = parseInt(args, 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ', number);
}
