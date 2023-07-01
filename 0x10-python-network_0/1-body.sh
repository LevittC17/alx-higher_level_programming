#!/bin/bash
# Usage: get url, display 200 response code
curl -sf -w "\n%{http_code}\n" "$1"
