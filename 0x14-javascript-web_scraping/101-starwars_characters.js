#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const film = JSON.parse(body);
    film.characters.forEach(function (character) {
      request(character, function (err, res, data) {
        if (err) console.log(err);
        else {
          const json = JSON.parse(data);
          console.log(json.name);
        }
      });
    });
  }
});
