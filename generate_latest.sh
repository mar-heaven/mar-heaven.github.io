#!/bin/bash

# Read the integer from the file into a variable
count=$(cat latest_id)

# Add 1 to the integer using the expr command
new_count=$(expr $count + 1)

# Write the new count back to the file
echo "$new_count" > latest_id
hexo new $new_count