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
# Where those files are absent, as in a Claude Code cloud session or on the
# GitHub runner, the lists come from the environment variables PRIVATE_NAMES and
# SENSITIVE_TOPICS instead, entries separated by newlines or commas.
#
# Matching ignores case and takes whole words only. The check reads the lines
# the commit adds, the paths of files it adds, and the commit message. It
# reports where a match is and never prints the matched text, so the names do
# not reach a terminal log, a build log or a Claude session.
#
# Runs as the commit-msg hook in .githooks; enable once per clone with
#
#     git config core.hooksPath .githooks
#
# After reviewing a topic match, commit again with PRIVACY_REVIEWED=1 set.
# There is no override for a name: edit the line.
#
# With --all it checks names only, across every tracked file, every path and
# every commit message, which is what the publish workflow runs:
#
#     _scripts/privacy-check.sh --all

set -uo pipefail
cd "$(dirname "$0")/.."

DIR=${TRINITY_PRIVATE_DIR:-$HOME/.config/trinitymetrics}
NAMES_FILE=$DIR/private-names.txt
TOPICS_FILE=$DIR/sensitive-topics.txt
GREP=/usr/bin/grep

MODE=commit
MSG=
case "${1:-}" in
  --all) MODE=all ;;
  *)     MSG=${1:-} ;;
esac

# Entries from a list file or, failing that, a variable; without comments,
# blank lines or stray whitespace.
entries() {
  local file=$1 value=$2
  if [ -f "$file" ]; then cat "$file"; else printf '%s\n' "$value" | tr ',' '\n'; fi |
    sed -e 's/\r$//' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' |
    $GREP -v -e '^#' -e '^$'
}

# Every line a commit would publish, as "location<TAB>text".
commit_candidates() {
  git diff --cached -U0 --no-color --no-ext-diff | awk '
    /^\+\+\+ / { file = substr($0, 7); next }
    /^@@ /     { split($3, a, ","); line = substr(a[1], 2) + 0; next }
    /^\+/      { print file ":" line "\t" substr($0, 2); line++ }'
  git diff --cached --name-only --diff-filter=AR | awk '{ print $0 " (path)\t" $0 }'
  if [ -n "$MSG" ] && [ -f "$MSG" ]; then
    $GREP -v '^#' "$MSG" | awk '{ print "commit message:" NR "\t" $0 }'
  fi
}

# Every path and commit message in the repository, as "location<TAB>text".
# File contents are searched separately by git grep, which reports its own
# locations.
all_candidates() {
  git ls-files | awk '{ print $0 " (path)\t" $0 }'
  git log --format='%h%x09%B' | awk -F'\t' '
    NF > 1 { commit = $1; print "commit " commit " message\t" $2; next }
           { print "commit " commit " message\t" $0 }'
}

# Locations matching any of the given patterns.
matches() {
  local patterns=$1
  [ -n "$patterns" ] || return 0
  if [ "$MODE" = all ]; then
    git grep -nIiwF -f <(printf '%s\n' "$patterns") | cut -d: -f1,2
    all_candidates | $GREP -iwF -f <(printf '%s\n' "$patterns") | cut -f1 | sort -u
  else
    commit_candidates | $GREP -iwF -f <(printf '%s\n' "$patterns") | cut -f1
  fi
}

report() {
  printf '%s\n' "$1" | sed 's/^/  /' >&2
}

status=0

names=$(entries "$NAMES_FILE" "${PRIVATE_NAMES:-}")
if [ -n "$names" ]; then
  hits=$(matches "$names")
  if [ -n "$hits" ]; then
    echo "privacy-check: a private name appears at:" >&2
    report "$hits"
    echo "Refer to the person by relationship instead." >&2
    status=1
  fi
else
  echo "privacy-check: no list of names found in $NAMES_FILE or PRIVATE_NAMES;" \
       "names were not checked." >&2
  # The runner has no excuse for a missing list, since it comes from a secret.
  [ "$MODE" = all ] && status=1
fi

topics=$(entries "$TOPICS_FILE" "${SENSITIVE_TOPICS:-}")
if [ "$MODE" = commit ] && [ -n "$topics" ] && [ "${PRIVACY_REVIEWED:-0}" != 1 ]; then
  hits=$(matches "$topics")
  if [ -n "$hits" ]; then
    echo "privacy-check: a sensitive topic appears at:" >&2
    report "$hits"
    echo "Review those lines, then commit again with PRIVACY_REVIEWED=1." >&2
    status=1
  fi
fi

exit $status
