#!/bin/bash 
# Sends a request to a URL passed as an argumen
curl -s -L -X HEAD -w "%{http_code}" "$1"
