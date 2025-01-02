#!/usr/bin/node
/**
 * A function  to print arguments already printed
 * @param {item} str - input
 * @returns void
 */
let args = 0;
exports.logMe = function (item) {
  console.log(`${args}: ${item}`);
  args++;
};
