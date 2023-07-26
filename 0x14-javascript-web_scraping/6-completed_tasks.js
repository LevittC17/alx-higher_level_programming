#!/usr/bin/node

// import the request module
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) return console.error(err);
  if (response.statusCode !== 200) return console.error('Error: Unable to fetch data from the provided API URL');

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
