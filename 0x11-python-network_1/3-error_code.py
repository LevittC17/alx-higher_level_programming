#!/usr/bin/python3
"""
Take in a URL
Send a request to the URL
Display the body of the response
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
