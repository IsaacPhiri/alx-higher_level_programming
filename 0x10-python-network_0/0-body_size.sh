#!/usr/bin/env bash
# A script that returns the number of bytes in an http reponse body
curl -s "$1" | wc -c
