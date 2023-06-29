#!/bin/bash
# Take a URL, send a request, display size of the body

response=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
