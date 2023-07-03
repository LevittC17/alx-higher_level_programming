#!/usr/bin/python3

"""
Fetching a url with urllib package
"""


import urllib.request

# Assign the given url to a url variable
url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

# Printing the response of the body
print('Body response:')
print('\t- type:', type(body))
print('\t- content:', body)
print('\t- utf8 content:', body.decode('utf-8'))
