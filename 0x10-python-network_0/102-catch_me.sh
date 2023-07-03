#!/bin/bash
# Make a request, server responds with a message
curl -s 0.0.0.0:5000/catch_me --request POST --data "user_id=98" --header "Origin: HolbertonSchool"
