#!/usr/bin/node

$(document).ready(function() {
  // jQuery code to add an <li> element to the <url> to the <ul> on click
  $('#add_item').click(function() {
    $('<li>Item</li>').appendTo('.my_list');
  });
});
