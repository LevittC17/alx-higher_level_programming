#!/bin/bash
# Make a request to 0.0.0.0:5000/catchme, server responds with a message
curl -s 0.0.0.0:5000/catch_me | grep -o "You got me!"
