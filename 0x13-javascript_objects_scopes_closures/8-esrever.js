#!/usr/bin/node

/**
 * Function to return reversed version of a list
 * reverse() not allowed
 * Using a for loop ...
*/

exports.esrever = function (list) {
  const newLst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newLst.push(list[i]);
  }
  return newLst;
};
