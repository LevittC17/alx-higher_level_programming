#!/bin/bash
# Send a GET request to URl
# Display only body of a 200 status code response

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# checking if status code == 200
if [ "$response" -eq 200 ]; then
  body=$(curl -s "$1")
  echo "$body"
fi
