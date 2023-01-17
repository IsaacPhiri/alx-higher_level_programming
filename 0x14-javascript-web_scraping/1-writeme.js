#!/usr/bin/node
'use strict';

const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite + '\n', { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  process.exit(0);
});
