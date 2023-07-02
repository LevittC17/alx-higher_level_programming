#!/bin/bash
# Make a request, server responds with a message
curl -sSL 0.0.0.0:5000/catch_me -X PUT -H "You got me!"
