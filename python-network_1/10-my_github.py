#!/usr/bin/python3
"""
A script that uses GitHub API to display an id using Basic Authentication.
The username and personal access token are passed as command-line arguments.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
