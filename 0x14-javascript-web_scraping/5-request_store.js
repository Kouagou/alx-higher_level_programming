#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;

request(argv[2]).pipe(fs.createWriteStream(argv[3]));
