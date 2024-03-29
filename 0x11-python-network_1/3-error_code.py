#!/usr/bin/python3
""" A Python script that takes in a URL, sends a request to the URL
    and displays the body of the response.
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
