#!/usr/bin/python3

"""
Take a URL and an email address
Send a POST request to the passed URL
parameter: email
Display the body of the response

"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
