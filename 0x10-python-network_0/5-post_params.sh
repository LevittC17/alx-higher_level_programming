#!/bin/bash

# Get the URL from the command-line argument
url=$1

# Set the email and subject parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Send the POST request with curl and display the response body
curl -s -X POST -d "email=$email&subject=$subject" "$url"

