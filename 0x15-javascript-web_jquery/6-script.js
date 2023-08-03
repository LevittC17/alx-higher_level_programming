#!/usr/bin/node

$(document).ready(function () {
  // Update the <header> text element on click
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
