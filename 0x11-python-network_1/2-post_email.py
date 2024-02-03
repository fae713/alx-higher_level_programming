#!/usr/bin/python3
""" a Python script that takes in a URL
    and an email, sends a POST request to
    the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email_add = {'email': sys.argv[2]}
    email_parse = urllib.parse.urlencode(email_add).encode("ascii")

    request = urllib.request.Request(url, email_parse)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
