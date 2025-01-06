#!/usr/bin/node
/**
 * function that reverse a list
 * @param {list} list - input
 * @returns {number} - the reversed version of a list
 */
exports.esrever = function (list) {
  const nlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    nlist.push(list[i]);
  }
  return nlist;
};
