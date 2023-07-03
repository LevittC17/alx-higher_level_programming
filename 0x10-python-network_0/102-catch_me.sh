#!/bin/bash
# Make a request, server responds with a message
curl -s -X POST http://0.0.0.0:5000/catch_me -o /dev/null -w "You got me!"
