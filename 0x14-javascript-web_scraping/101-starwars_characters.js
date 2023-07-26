#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const endPoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(endPoint, (err, response, body) => {
  if (err) return console.error(err);
  if (response.statusCode !== 200) return console.error(`Error: Unable to fetch movie with ID ${movieID}`);

  const charUrls = JSON.parse(body).characters;

  const fetchCharacterData = (characterUrl) => new Promise((resolve, reject) => {
    request.get(characterUrl, (charErr, charResponse, charBody) => {
      if (charErr) reject(charErr);
      else resolve(JSON.parse(charBody).name);
    });
  });

  Promise.all(charUrls.map(fetchCharacterData))
    .then((characterNames) => characterNames.forEach((name) => console.log(name)))
    .catch((error) => console.error(error));
});
