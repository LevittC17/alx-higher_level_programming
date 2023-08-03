#!/usr/bin/node

$(document).ready(function () {
  // jQuery code to add the class `red` to the <header> element on click
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
