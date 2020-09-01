#!/bin/bash
if [ "$1" ]
then
  git add .
  git commit -m "$1"
  git push
else
  echo Please specify commit message
fi
