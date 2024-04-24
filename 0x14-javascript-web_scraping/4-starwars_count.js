#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) console.log(error);
  else {
    const json = JSON.parse(body);
    let count = 0;
    const arr = json.results;
    for (const el of arr) {
      for (const i of el.characters) {
        if (i.includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
