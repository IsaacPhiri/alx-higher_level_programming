#!/usr/bin/node
'use strict';

const request = require("request");
const url = process.argv[2];

let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error("Error: ", error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    let data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes("18")) {
          count++;
        }
      });
    });
    console.log(`Wedge Antilles is present in ${count} movies.`);
    process.exit(0);
  } else {
    console.error("Invalid status code: ", response.statusCode);
    process.exit(1);
  }
});
