#!/usr/bin/node

const request = require('request');

const endPoint = process.argv[2];

request.get(endPoint, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const tasks = JSON.parse(body);
      const userCompletedTasks = {};

      tasks.forEach((tasks) => {
        if (tasks.completed) {
          if (userCompletedTasks[tasks.userId]) {
            userCompletedTasks[tasks.userId]++;
          } else {
            userCompletedTasks[tasks.userId] = 1;
          }
        }
      });

      console.log(userCompletedTasks);
    } else {
      console.error('Error: Unable to fetch data from the API URL');
    }
  }
});
