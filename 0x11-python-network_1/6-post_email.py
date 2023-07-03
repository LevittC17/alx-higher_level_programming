#!/usr/bin/python3

"""
Get URL and email address, send a POST request
with the email as parameter
display body response
"""


import sys
import requests


def main():
    # Fetch the url and email address
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={"email": email})
    print(response.text)


if __name__ == "__main__":
    main()
