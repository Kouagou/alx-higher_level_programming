#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response) {
  if (error) console.log(error);
  else console.log('code:', response.statusCode);
});
