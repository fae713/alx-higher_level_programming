#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
 using urllib

"""

if __name__ == "__main____":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    response = urllib.request.urlopen(url)
    read_body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(read_body)))
    print("\t- content: {}".format(read_body))
    print("\t- utf8 content: {}".format(read_body.decode('utf-8')))
