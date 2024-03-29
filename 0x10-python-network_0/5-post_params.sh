#!/bin/bash
# A script that takes in a URL, sends a POST requestand displays the body.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
