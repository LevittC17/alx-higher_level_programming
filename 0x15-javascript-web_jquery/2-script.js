#!/usr/bin/node

$(document).ready(function () {
  // jQuery code  to update the text color of the <header> element to red
  // when the div is clicked
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
