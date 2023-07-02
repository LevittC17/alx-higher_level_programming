#!/bin/bash
# Make a request to 0.0.0.0:5000/catchme, server responds with a message
curl -sL -X PUT -H "You got me!" 0.0.0.0:5000/catch_me
