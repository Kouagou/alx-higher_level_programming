#!/usr/bin/node
const num = Number(process.argv[2]);
for (let i = 0; i < num; i++) {
  let str = '';
  for (let j = 0; j < num; j++) {
    str += 'X';
  }
  console.log(str);
}
