#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 * check if `w` and `h` are eqaul to 0 or not a positive integer
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
