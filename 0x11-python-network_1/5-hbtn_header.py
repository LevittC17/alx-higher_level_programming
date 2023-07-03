#!/usr/bin/python3

"""
send a request to a URL and dispay the
variable X-Request_id
use requests package
"""


import requests
import sys


def main():
    # fetch the URL
    url = sys.argv[1]

    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)


if __name__ == "__main__":
    main()
