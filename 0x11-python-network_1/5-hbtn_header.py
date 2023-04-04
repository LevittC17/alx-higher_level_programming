#!/usr/bin/python3

"""
Take a URL and send a request to it
Display the value of the variable X-Request_Id 
in the response header
"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
