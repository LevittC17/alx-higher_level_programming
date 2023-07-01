#!/bin/bash
# Display all HTTP methods the server will accept
curl -sIL "$1" | grep -i "^allow:" | awk -F ": " '{print $2}'
