#!/bin/bash
# Make a request, server responds with a message
curl -s -X PUT -H "Origin: HolbertonSchool" --data "user_id=98" "0.0.0.0:5000/catch_me
