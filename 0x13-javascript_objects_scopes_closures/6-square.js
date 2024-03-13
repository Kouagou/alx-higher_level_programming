#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        console.log(str);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
