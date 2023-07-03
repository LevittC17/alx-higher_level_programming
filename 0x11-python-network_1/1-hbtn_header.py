#!/usr/bin/python3

"""
Send a request to a URL and display
the value of the x-Request-Id varible
in the header response
"""


import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-Id')

print(request_id)
