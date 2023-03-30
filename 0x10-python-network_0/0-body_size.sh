#!/bin/bash

url=$1

# Send a GET request to the specified URL and store the response body in a variable
response=$(curl -s -w '\n%{size_download}\n' "$url")

# Extract the size of the response body from the response variable
size=$(echo "$response" | tail -1)

# Display the size of the response body in bytes
echo "The size of the response body is $size bytes."
