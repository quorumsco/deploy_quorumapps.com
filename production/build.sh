#!/bin/bash

if [ "$#" -eq 0 ]; then
  repos=("node-ruby" "frontdev" "quorumapps.com" "siteweblisa")
else
  repos=$*
fi

for i in ${repos[@]}; do
  #(cd "images/$i" && git checkout master && git remote update -p && git merge --ff-only @{u})
  rm -rf "images/$i"
  git clone https://github.com/quorumsco/$i.git images/$i
  docker rmi -f quorum/$i:latest
  docker build -t quorum/$i:latest images/$i
  docker push quorum/$i:latest
done
