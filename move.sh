#!/bin/bash
count=$(cat latest_id)
file=source/_posts/${count}-en.md
mv ${file} source/weekly