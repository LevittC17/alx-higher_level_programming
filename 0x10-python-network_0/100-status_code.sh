#!/bin/bash
# GET request, no redirections
curl -s -o /dev/null -w "%{http_code}" "$1"
