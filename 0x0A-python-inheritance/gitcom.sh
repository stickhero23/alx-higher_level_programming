#!/bin/bash

#Check if a commit message was provided
if [ $# -eq 0 ]; then
  echo "Error: No commit message provided"
  exit 1
fi

# Add all changes in the current directory
git add .

# Commit the changes with the provided message
git commit -m "$1"

# Push the changes to the remote repository
git push

