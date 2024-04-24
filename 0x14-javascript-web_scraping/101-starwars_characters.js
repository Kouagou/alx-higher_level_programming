#!/usr/bin/node
const request = require('request');
const argv = process.argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const results = [];
    const film = JSON.parse(body);
    film.characters.forEach(function (character, index) {
      request(character, function (err, res, data) {
        if (err) console.log(err);
        else {
          const json = JSON.parse(data);
          results[index] = json.name;
          if (results.filter(Boolean).length === film.characters.length) {
            results.forEach(name => console.log(name));
          }
        }
      });
    });
  }
});
