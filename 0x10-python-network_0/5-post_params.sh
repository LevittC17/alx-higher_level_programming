#!/bin/bash
# Send a POST request to the passed URL with key:value pairs
curl -sSL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
