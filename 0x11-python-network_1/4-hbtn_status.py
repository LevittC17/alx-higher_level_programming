#!/usr/bin/python3

"""
Fetching https://alx-intranet.hbtn.io/status
package requests
"""


import requests

# Fetch the url
url = 'https://alx-intranet.hbtn.io/status'

# Use requests package
response = requests.get(url)
body = response.text

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
