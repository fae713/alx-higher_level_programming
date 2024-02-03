#!/usr/bin/python3
"""Listing 10 commits in a repo"""

import sys
import requests
import json

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        repository = sys.argv[2]
        url = f'https://api.github.com/repos/{username}/{repository}/commits'
        response = requests.get(url)
        response.raise_for_status() # Raises a HTTPError if the status is 4xx, 5xx
        commits = response.json()
        pretty_commits = json.dumps(commits[:10], indent=4)
        print(pretty_commits)
        for commit in commits[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)
