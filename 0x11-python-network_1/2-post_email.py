#!/usr/bin/python3

"""
send a POST request to a URL with
email as a parameter and display the
body of the respobse(decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys


def main():
    # Fetch the url and email
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    try:
        with urllib.request.urlopen(url, data) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    main()
