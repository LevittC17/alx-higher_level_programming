#!/usr/bin/node

const request = require('request');

const endPoint = process.argv[2];
const charId = 18;

request.get(endPoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body);
      const filmsWithChar = filmsData.results.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)
      );
      console.log(filmsWithChar.length);
    } else {
      console.error('Error: Unable to fetch data from the Star Wars API');
    }
  }
});
