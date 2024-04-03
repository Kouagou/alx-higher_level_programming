#!/usr/bin/python3
""" A Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    res = requests.post(url, data={"q": letter})
    try:
        body = res.json()
        if body == {}:
            print("No result")
        else:
            print("[{}] {}".format(body.get("id"), body.get("name")))
    except ValueError:
        print("Not a valid JSON")
