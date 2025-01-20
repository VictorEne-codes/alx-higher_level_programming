#!/bin/bash
# script that takes in a URL and sends a rewuest to the URL
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
