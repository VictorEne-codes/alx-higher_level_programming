#!/usr/bin/node
const args = process.argv;
if (!isNaN(args[2])) {
  for (let i = 1; i <= args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
