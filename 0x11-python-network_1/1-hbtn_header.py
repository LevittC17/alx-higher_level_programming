#!/usr/bin/python3

"""
Get the URL from the
command-line argument
"""
import urllib.request
import sys

url = sys.argv[1]

# Send a request to the URL
req = urllib.request.Request(url)

# Open the connection and send the request
with urllib.request.urlopen(req) as response:
    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')
    # Display the value of the X-Request-Id header
    print(x_request_id)
