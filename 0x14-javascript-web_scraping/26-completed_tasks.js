#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const results = {};
    const users = new Set();
    for (const todo of todos) {
      users.add(todo.userId);
    }

    for (const user of users) {
      let count = 0;
      for (const todo of todos) {
        if (user === todo.userId && todo.completed === true) {
          count++;
        }
      }
      results[user] = count;
    }
    console.log(results);
  }
});
