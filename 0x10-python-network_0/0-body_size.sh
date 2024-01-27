#!/bin/bash

[ $# -eq 0 ] && { echo "Usage: $0 <URL>"; exit 1; }

curl -sI "$1" | awk '/^Content-Length:/ {print "Size of the response body:", $2, "bytes"}'
