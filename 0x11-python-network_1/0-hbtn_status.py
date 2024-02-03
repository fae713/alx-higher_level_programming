#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
 using urllib

"""


if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        read_body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(read_body)))
        print("\t- content: {}".format(read_body))
        print("\t- utf8 content: {}".format(read_body.decode('utf-8')))
