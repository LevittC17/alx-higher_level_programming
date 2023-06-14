#!/usr/bin/node

/**
 * class Square that defines a square
 * inherits from the class Rectangle in 4-rectangle.js
*/

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
