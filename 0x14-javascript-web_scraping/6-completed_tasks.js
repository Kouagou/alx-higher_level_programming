#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
	  return;
  }
  const todos = JSON.parse(body);
  const results = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (!results[todo.userId]) {
        results[todo.userId] = 1;
      } else {
        results[todo.userId] += 1;
      }
    }
  });
  console.log(results);
});
