#!/usr/bin/node

$(document).ready(function () {
  // Fetch and display the translation of `hello`
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('hello').text(data.hello);
  });
});
