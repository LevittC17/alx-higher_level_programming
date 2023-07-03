#!/usr/bin/python3

"""
send a request to a URL, display response body
managing urllib.error.HTTPError
"""


import urllib.request
import urllib.error
import sys


def main():
    # Get URL from sys argument
    url = sys.argv[1]

    # Using a try except block
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().encode('utf-8')
            print('Body response:')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)


if __name__ == "__main__":
    main()
