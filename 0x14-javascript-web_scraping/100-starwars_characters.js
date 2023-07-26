#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(endPoint, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const movieDT = JSON.parse(body);
      const charUrls = movieDT.characters;

      charUrls.forEach((characterUrl) => {
        request.get(characterUrl, (charErr, charResponse, charBody) => {
          if (charErr) {
            console.error(charErr);
          } else {
            if (charResponse.statusCode === 200) {
              const charDT = JSON.parse(charBody);
              console.log(charDT.name);
            } else {
              console.error('Error: Unable to fetch character data from the Star Wars API');
            }
          }
        });
      });
    } else {
      console.error(`Error: Unable to fetch movie with ID ${movieID}`);
    }
  }
});
