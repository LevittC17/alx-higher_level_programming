#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 * instance method print() - print rectangle with 'X' character
 * instance method rotate() - swap width `w` and height `h`
 * instance method double() - multiply each width and height by 2
*/

class Rectangle {
  constructor (w, h) {
    // check if w, h = 0 or < 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }

    this.double = function () {
      this.width *= 2;
      this.height *= 2;
    };

    this.rotate = function () {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    };

    this.print = function () {
      // Iterate through width and height
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    };
  }
}

module.exports = Rectangle;
