#!/bin/bash
# Send a DELETE request to the URL passed, display body response
curl -sSL -X DELETE "$1" | awk -v RS= '{$1=$1}1' | sed -n 's/.*\r\n\r\n\(.*\)/\1/p'
