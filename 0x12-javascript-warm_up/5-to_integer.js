#!/usr/bin/node
const args = process.argv;
if (!isNaN(args[2])) {
  console.log('My number: ' + String(parseInt(args[2])));
} else {
  console.log('Not a number');
}
