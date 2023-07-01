#!/bin/bash
# send a request to an URL with curl, display body response size
curl -s "$1" | wc -c
