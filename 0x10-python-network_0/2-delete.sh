#!/bin/bash

url=$1

curl -X DELETE -s -o /dev/null -w "%{http_code}\n" "$url" | 
  if grep -q "^2"; then
    curl -X DELETE -s "$url"
  else
    echo "Failed to delete $url"
  fi
