#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(endPoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Error: Unable to fetch movie wth ID ${movieID}`);
    }
  }
});
