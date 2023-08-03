#!/usr/bin/node

$(document).ready(function() {
  // jQuery code to toggle the class of the <header> element on click
  $('#toggle_header').click(function() {
    $('header').toggleClass('red green');
  });
});
