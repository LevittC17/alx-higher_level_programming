#!/bin/bash
# Take a URL, send a request, display size of the body

curl -s "$1" | wc -c
