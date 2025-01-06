#!/usr/bin/node
const args = process.argv;
if (!isNaN(args[2])) {
  for (let i = 1; i <= args[2]; i++) {
    let row = '';
    for (let j = 1; j <= args[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
