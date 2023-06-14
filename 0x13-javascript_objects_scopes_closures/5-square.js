#!/usr/bin/node

/**
 * class Square that defines a square
 * inherits from the class Rectangle in 4-rectangle.js
*/

import { Rectangle } from './4-rectangle.js';

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(Rectangle);
    this.size = size;
  }
};
