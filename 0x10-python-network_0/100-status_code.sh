#!/bin/bash
# A Bash script that sends a request to a URL, and displays status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
