#!/usr/bin/node
const args = process.argv;
if (!isNaN(args[2])) {
  console.log(parseInt(args[2]));
} else {
  console.log('Not a Number');
}
