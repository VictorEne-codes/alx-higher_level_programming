#!/usr/bin/node
/**
 * A function to convert from base 10 to another base
 * @param {number} base - input
 * @returns {any} - the number converted to given
 */
exports.converter = function (base) {
  function converted (number) {
    return number.toString(base);
  }
  return converted;
};
