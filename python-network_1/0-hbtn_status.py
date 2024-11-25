#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status and http://0.0.0.0:5050/status.
"""

import urllib.request

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))

with urllib.request.urlopen('http://0.0.0.0:5050/status') as response:
    body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
