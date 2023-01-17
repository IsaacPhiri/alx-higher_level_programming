#!/usr/bin/node
'use strict';

const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(`Error: ${error.code}`);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
  process.exit(0);
});
