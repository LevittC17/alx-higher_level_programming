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
    # Get url and email values
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

        print('Your email is:', body)


if __name__ == "__main__":
    main()
