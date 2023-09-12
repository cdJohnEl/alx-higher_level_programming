#!/usr/bin/node
/**
 * Square class that inherits from rectangle class
 */

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
