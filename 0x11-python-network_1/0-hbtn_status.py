#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status

"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
response = urllib.request.urlopen(url)
body_content = response.read()
print(f"""
- type: {type(body_content)}
- content: {body_content}
- utf8 content: {body_content.decode("utf-8")}
""")
