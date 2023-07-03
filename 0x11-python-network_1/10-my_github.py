#!/usr/bin/python3

"""
Get GitHub credentials, use the GitHub API
to display the Id
"""

import requests
import sys


def main():
    # Fetch the username and access token
    username = sys.argv[1]
    token = sys.argv[2]

    # Fetch the GitHub API URL
    url = 'https://api.github.com/user'

    # Pass the personal access token as a header
    headers = {
        'Authorization': 'token {}'.format(token),
        'Accept': 'application/vnd.github.v3+json'
    }

    # Retreive json data and store it in data variable
    response = requests.get(url, headers=headers)
    data = response.json()

    # Print specific fields from the response
    if 'id' in data:
        print(data['id'])
    else:
        print('None')


if __name__ == "__main__":
    main()
