#!/usr/bin/env bash

echo "Add last Coderegation video as blog post automatically."


if [ -z "$1" ]; then
    echo "ERROR: The first parameter must be the issue id in GitHub"
    exit 1
fi

issue_id="$1"

cd "$( dirname "${BASH_SOURCE[0]}" )"

echo
echo "Downloading..."
./download.py --id "$issue_id"

echo
echo "Converting..."
./convert.py

cd ..
echo
git status
echo
echo "Press ENTER to commit every post"
read
git add _posts
git commit -sm "New video, closes #$issue_id"

