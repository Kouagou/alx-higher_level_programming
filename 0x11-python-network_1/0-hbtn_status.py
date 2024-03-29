#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """
from urllib.request import urlopen


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("    - type {}:".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode("utf-8")))
