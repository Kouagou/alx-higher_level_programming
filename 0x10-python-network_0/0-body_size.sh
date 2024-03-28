#!/bin/bash
# A script that sends a request to a URL and displays the size of the body.
curl -s "$1" | wc -c
