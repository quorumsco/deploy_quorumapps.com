#!/bin/bash

if [ "$#" -eq 0 ]; then
  repos=("node-ruby" "frontdev" "quorumapps.com")
else
  repos=$*
fi

for i in ${repos[@]}; do
  docker pull quorum/$i:latest
done
