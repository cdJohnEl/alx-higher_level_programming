#!/usr/bin/node
const firstArg = process.argv[2];
const number = parseInt(firstArg);

if (!isNaN(number)) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
