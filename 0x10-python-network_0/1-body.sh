#!/bin/bash

url=$1

# Send GET request to URL and store response in variable
response=$(curl -sSL -w "%{http_code}" "$url")

# Check if response status code is 200
if [[ $response == "200"* ]]; then
  # Display response body
  curl -sSL "$url"
else
  echo "Error: $response"
fi
