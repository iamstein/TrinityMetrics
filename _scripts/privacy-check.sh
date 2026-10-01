#!/usr/bin/env bash
#
# Stop a commit that names a family member or touches a sensitive topic.
#
# The repository is public, so a name in any committed line is public even if
# the page never renders. The lists of names and topics cannot live here for the
# same reason; they are kept outside the repository, one entry per line:
#
#     ~/.config/trinitymetrics/private-names.txt      blocks the commit
#     ~/.config/trinitymetrics/sensitive-topics.txt   holds it for review
#
# Matching ignores case and takes whole words only. The check reads the lines
# the commit adds, the paths of files it adds, and the commit message. It
# reports where a match is and never prints the matched text, so the names do
# not reach a terminal log or a Claude session.
#
# Runs as the commit-msg hook in .githooks; enable once per clone with
#
#     git config core.hooksPath .githooks
#
# After reviewing a topic match, commit again with PRIVACY_REVIEWED=1 set.
# There is no override for a name: edit the line.

set -uo pipefail
cd "$(dirname "$0")/.."

DIR=${TRINITY_PRIVATE_DIR:-$HOME/.config/trinitymetrics}
NAMES=$DIR/private-names.txt
TOPICS=$DIR/sensitive-topics.txt
MSG=${1:-}
GREP=/usr/bin/grep

# Every line the commit would publish, as "location<TAB>text".
candidates() {
  git diff --cached -U0 --no-color --no-ext-diff | awk '
    /^\+\+\+ / { file = substr($0, 7); next }
    /^@@ /     { split($3, a, ","); line = substr(a[1], 2) + 0; next }
    /^\+/      { print file ":" line "\t" substr($0, 2); line++ }'
  git diff --cached --name-only --diff-filter=AR | awk '{ print $0 " (path)\t" $0 }'
  if [ -n "$MSG" ] && [ -f "$MSG" ]; then
    $GREP -v '^#' "$MSG" | awk '{ print "commit message:" NR "\t" $0 }'
  fi
}

# Entries from a list, without comments, blank lines or stray whitespace.
entries() {
  sed -e 's/\r$//' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' "$1" |
    $GREP -v -e '^#' -e '^$'
}

# Locations of candidate lines matching any entry in a list.
matches() {
  local list=$1 patterns
  patterns=$(entries "$list")
  [ -n "$patterns" ] || return 0
  candidates | $GREP -iwF -f <(printf '%s\n' "$patterns") | cut -f1
}

status=0

if [ -f "$NAMES" ]; then
  hits=$(matches "$NAMES")
  if [ -n "$hits" ]; then
    echo "privacy-check: a name from $NAMES appears at:" >&2
    printf '%s\n' "$hits" | sed 's/^/  /' >&2
    echo "Refer to the person by relationship instead. Commit blocked." >&2
    status=1
  fi
else
  echo "privacy-check: $NAMES not found; names were not checked." >&2
fi

if [ -f "$TOPICS" ] && [ "${PRIVACY_REVIEWED:-0}" != 1 ]; then
  hits=$(matches "$TOPICS")
  if [ -n "$hits" ]; then
    echo "privacy-check: a sensitive topic from $TOPICS appears at:" >&2
    printf '%s\n' "$hits" | sed 's/^/  /' >&2
    echo "Review those lines, then commit again with PRIVACY_REVIEWED=1." >&2
    status=1
  fi
fi

exit $status
