#!/usr/bin/env bash
#
# Set each tracked .qmd file's modification time to its last commit.
#
# Pages carrying `date: last-modified` take the date from the file's mtime.
# A fresh checkout stamps every file with the checkout time, so without this
# step every page on the site shows the day of the build. Run it after a
# checkout with full history (fetch-depth: 0). Uses GNU touch, as on the runner.

set -euo pipefail

git ls-files -z '*.qmd' | while IFS= read -r -d '' f; do
  ts=$(git log -1 --format=%ct -- "$f")
  [ -n "$ts" ] && touch -d "@$ts" "$f"
done
