#!/usr/bin/env bash
#
# Check that every project folder has exactly one card, and every card a target.
#
# A folder under projects/ is reachable from the site only through a card in
# projects/projects.yml, which builds the Projects page, or projects/archive.yml,
# which builds the Archive page. A folder with no card still renders and still
# publishes, but nothing links to it, so it is findable only by guessing the
# URL. That happened to projects/site-integration and went unnoticed for weeks,
# which is why this script exists.
#
#     _scripts/check-project-cards.sh
#
# Exits non-zero on the first kind of problem found, so it can gate a build.

set -uo pipefail
cd "$(dirname "$0")/.."

PROJECTS=projects/projects.yml
ARCHIVE=projects/archive.yml
status=0

note() { printf '  %s\n' "$1"; }

# Local card targets, one per line, as "file<TAB>source-yml".
cards() {
  for f in "$PROJECTS" "$ARCHIVE"; do
    grep -E '^[[:space:]]*path:' "$f" \
      | sed -E 's/^[[:space:]]*path:[[:space:]]*//' \
      | grep -v '^https\?://' \
      | while read -r p; do printf '%s\t%s\n' "$p" "$f"; done
  done
}

# A project folder is one holding an index.qmd. Quarto writes build directories
# such as projects/index_files/ alongside them, and those are not projects.
echo "Folders under projects/ with no card"
found=0
for d in projects/*/; do
  name=$(basename "$d")
  case "$name" in *_files|.*) continue;; esac
  if [ ! -f "$d/index.qmd" ]; then
    note "$name  (no index.qmd; every project folder carries one)"
    found=1; status=1
    continue
  fi
  if ! cards | cut -f1 | grep -qx "$name/index.qmd"; then
    note "$name  (add a card to $PROJECTS or $ARCHIVE)"
    found=1; status=1
  fi
done
[ "$found" -eq 0 ] && note "none"

echo "Folders carrying a card in both files"
dupes=$(cards | cut -f1 | sort | uniq -d)
if [ -n "$dupes" ]; then
  printf '%s\n' "$dupes" | while read -r p; do note "$p  (remove one)"; done
  status=1
else
  note "none"
fi

echo "Cards pointing at a file that does not exist"
missing=0
while IFS=$'\t' read -r p src; do
  [ -z "$p" ] && continue
  if [ ! -f "projects/$p" ] && [ ! -f "$(cd projects && realpath -m "$p" 2>/dev/null)" ]; then
    note "$p  (named in $src)"
    missing=1; status=1
  fi
done < <(cards)
[ "$missing" -eq 0 ] && note "none"

echo
if [ "$status" -eq 0 ]; then
  echo "OK: every project folder has exactly one card, and every card a target."
else
  echo "FAIL: see above."
fi
exit "$status"
