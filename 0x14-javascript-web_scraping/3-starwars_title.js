#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
