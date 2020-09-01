#!/bin/bash
if [ "$1" ]
then
  git add .
  git commit -m '"$@"'
  git push
else
  echo Please specify commit message
fi
