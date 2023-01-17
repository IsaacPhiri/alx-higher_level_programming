#!/usr/bin/node
'use strict';

const request = require("request");
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error("Error: ", error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    let data = JSON.parse(body);
    console.log(data.title);
    process.exit(0);
  } else {
    console.error("Invalid status code: ", response.statusCode);
    process.exit(1);
  }
});
