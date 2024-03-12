#!/usr/bin/node
const len = process.argv.length;
const argv = process.argv;
if (len <= 3) {
  console.log(0);
} else {
  let max = argv[2];
  let min = argv[3];
  if (max < min) {
    max = argv[3];
    min = argv[2];
  }
  for (let i = 3; i < len; i++) {
    if (max < argv[i]) {
      min = max;
      max = argv[i];
    } else if (min < argv[i]) {
      min = argv[i];
    }
  }
  console.log(min);
}
