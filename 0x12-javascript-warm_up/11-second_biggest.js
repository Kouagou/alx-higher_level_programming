#!/usr/bin/node
const len = process.argv.length;
const argv = process.argv;
if (len <= 3) {
  console.log(0);
} else {
  let max = Number(argv[2]);
  let min = Number(argv[3]);
  if (max < min) {
    max = Number(argv[3]);
    min = Number(argv[2]);
  }
  for (let i = 4; i < len; i++) {
    if (max < Number(argv[i])) {
      min = max;
      max = Number(argv[i]);
    } else if (min < Number(argv[i])) {
      min = Number(argv[i]);
    }
  }
  console.log(min);
}
