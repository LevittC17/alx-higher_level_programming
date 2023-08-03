#!/usr/bin/node

$(document).ready(function() {
  // Fetch character name from URL and display in the div
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    $('#character').text(data.name);
  });
});
