#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body resp
curl -s "$1" -X GET -L
