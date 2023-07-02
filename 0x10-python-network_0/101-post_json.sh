#!/bin/bash
# Send a JSON POST request with the contents of a file
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
