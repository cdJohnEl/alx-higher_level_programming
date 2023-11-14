#!/usr/bin/node

const list = require('./100-data').list;

const list2 = list.map((item, idx) => item * idx);
console.log(list);
console.log(list2);
