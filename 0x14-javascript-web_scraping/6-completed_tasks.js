#!/usr/bin/node

// import the request module
const request = require('request');

// API endPoint passed as the first argument
const endPoint = process.argv[2];

request.get(endPoint, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    for (const task of tasks) {
      const { completed, userId } = task;

      if (completed) {
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    }

    console.log(completedTasksByUser);
  }
});
