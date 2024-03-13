#!/usr/bin/node
exports.esrever = function (list) {
  const n = list.length;
  for (let i = 0; i < (n / 2); i++) {
    const tmp = list[i];
    list[i] = list[n - i - 1];
    list[n - i - 1] = tmp;
  }
  return list;
};
