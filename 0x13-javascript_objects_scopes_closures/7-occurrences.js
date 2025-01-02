#!/usr/bin/node
/**
 * function to count occurrences
 * @param {list} list - input
 * @param {number} searchElement - input
 * @returns {number} - the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};
