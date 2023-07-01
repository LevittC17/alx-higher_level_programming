#!/bin/bash
# Usage: get url, display 200 response code
curl -si "$1" | grep -oP "(?<=\r\n\r\n).*"
