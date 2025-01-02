#!/usr/bin/node

/**
 * script that imports a dictionary of occurrences by user id 
 * Print the new dictionary at the end
 */
const initDict = require('./101-data').dict;
const newDict = {};

for (const key in initDict) {
  if (newDict[initDict[key]] === undefined) {
    newDict[initDict[key]] = [];
  }
  newDict[initDict[key]].push(key);
}
console.log(newDict);
