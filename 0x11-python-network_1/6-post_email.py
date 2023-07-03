#!/usr/bin/python3

"""
Get URL and email address, send a POST request
with the email as parameter
display body response
"""


import requests
import sys


def main():
    # get URL and email
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print('Your email is:', email)


if __name__ == "__main__":
    main()
