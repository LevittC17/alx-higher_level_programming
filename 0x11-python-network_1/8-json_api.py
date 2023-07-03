#!/usr/bin/python3

"""
Take a letter and send a POST request to a
URL with the letter as parameter
"""

import requests
import sys


def main():
    # Fetch the URL and letter
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ''

    # dictionary to store the letter
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
