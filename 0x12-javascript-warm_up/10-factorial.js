#!/usr/bin/node
const num = Number(process.argv[2]);
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (num) {
  const fact = factorial(num);
  console.log(fact);
} else {
  console.log(1);
}
