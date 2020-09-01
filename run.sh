#!/bin/bash
# python3 test.py
# python3 main.py
# rmdir /home/sam/Desktop/Cleaned

if [ $1 = g ]
then
  if [ "$2" ]
  then
    git add .
    git commit -m "$2"
    git push
  else
    echo Please specify commit message
  fi
fi