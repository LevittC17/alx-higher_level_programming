#!/usr/bin/node

/**
 * Function to return reversed version of a list
 * reverse() not allowed
 * Using a for loop ...
*/

exports.esrever = function (list) {
  let newStr = '';
  for (let i = list.length - 1; i >= 0; i--) {
    newStr += list[i];
  }
  return newStr;
};
