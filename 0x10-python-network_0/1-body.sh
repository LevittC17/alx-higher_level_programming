#!/bin/bash
# Display the body of the response 200 from the url
curl -sf -w "\n%{http_code}\n" "$1"
