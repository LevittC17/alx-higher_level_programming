#!/usr/bin/node

$(document).ready(function() {
  // Fetch and list movie titles
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    const movies = data.results
    const $listMovies = $('#list_movies');

    movies.forEach(function(movie) {
      $('<li>').text(movie.title).appendTo($listMovies);
    });
  });
});
