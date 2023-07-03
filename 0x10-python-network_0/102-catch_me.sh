#!/bin/bash
# Make a request, server responds with a message
curl -s -X POST -H "Referer: 0.0.0.0:5000/catch_me" 0.0.0.0:5000/catch_me
