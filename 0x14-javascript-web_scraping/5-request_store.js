#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (writeErr) => {
        if (writeErr) {
          console.error(writeErr);
        }
      });
    } else {
      console.error('Error: Unable to fetch data from the URL');
    }
  }
});
