#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))
