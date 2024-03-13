#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c.toString();
        }
        console.log(str);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
