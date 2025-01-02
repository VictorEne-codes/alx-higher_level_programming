#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * @property {method} print - prints the rectangle using the character X
   * @returns void
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  /**
   * @property {method} rotate - this function will exchange w and h
   * @returns void
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * @property {method} double - this methos will display multiples of w and h
   * @returns void
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
