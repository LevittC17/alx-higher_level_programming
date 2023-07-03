#!/usr/bin/python3

"""
send a request to a URL and display response body
if HTTP status code is > 400, print Error code
use requests package
"""


import requests
import sys


def main():
    # fetch the url
    url = sys.argv[1]

    response = requests.get(url)
    body = response.text

    # Check if status_code is >= 400
    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        print(body)


if __name__ == "__main__"
    main()
