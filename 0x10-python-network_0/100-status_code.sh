#!/bin/bash
url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
echo "$response"
