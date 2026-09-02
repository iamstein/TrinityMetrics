#!/usr/bin/env bash
#
# Mirror the site's Google Docs and Slides as PDFs.
#
# Several of the readers of this site are on corporate networks that block
# Google Docs, so every Doc the site links to is also published here as a PDF.
# The Doc stays the editable copy and nobody has to remember to export it: the
# PDF is refetched on every build, so it is never stale, and it is written into
# the rendered site rather than committed, so it never enters git history.
#
# Run after `quarto render`, so the export lands in the rendered site:
#
#     _scripts/export-google-docs.sh [output-dir]     # default docs/files
#
# A Doc exports over plain HTTP only while it is shared as "anyone with the
# link, Viewer". A Doc that is not returns Google's sign-in page with a 200,
# which is why this checks the magic bytes rather than trusting the status
# code — an HTML sign-in page saved as a .pdf is the failure nobody notices.

set -euo pipefail

out_dir="${1:-docs/files}"

# kind | file id | published name. `kind` is document or presentation, matching
# the Google URL the Doc lives at.
exports=(
  "document|1gl52JUJqrf8wL0irCn-mFp_pw0Z5w0ZalvLnKw9GSyc|stein-cv.pdf"
  "document|1Hc3RoTJXS-PQCUm-rG_RCuEa3ykRj5FiAtqRwgSiX6M|causality-checklist.pdf"
  "document|1jtZHKJ88PEjVr2mxWzNjG51t97CyO8rv4zoenTH_RWE|how-to-read-a-paper.pdf"
  "document|1K_lcsG6sClLQcd5sm_ezcvtD9ccmm0uM|presentation-evaluation-form.pdf"
  "document|1678jBK-ffeoPMD2Q6nR-Dn8N8HnyJE1NEoF9enf8GUA|communication-methods.pdf"
  "document|1cuONopvVPAjFoieWZ13et9CjJ8DAcvmhuOFwGG31-z4|holding-people-accountable.pdf"
  "document|17ec8YaARWZ6wppv3AfZCdaHfPwvOFUABXyXmENgHnpE|r-coding-checklist.pdf"
  "document|1eXmTy0NHVlU1x5V-xzxwAPEHgYFjMzk8KvhF7gB0R98|learning-checklist-template.pdf"
  "document|1Y4-67r5LTs7tPChldFc_ZX-GO4dpzybt|career-feedback-form.pdf"
)

mkdir -p "$out_dir"
failed=0

for entry in "${exports[@]}"; do
  IFS='|' read -r kind id name <<< "$entry"

  case "$kind" in
    document)     url="https://docs.google.com/document/d/$id/export?format=pdf" ;;
    presentation) url="https://docs.google.com/presentation/d/$id/export/pdf" ;;
    *) echo "unknown kind '$kind' for $name" >&2; failed=1; continue ;;
  esac

  target="$out_dir/$name"

  if ! curl --fail --silent --show-error --location "$url" -o "$target"; then
    echo "export failed: $name ($id)" >&2
    failed=1
    continue
  fi

  if [ "$(head -c 4 "$target")" != "%PDF" ]; then
    echo "not a PDF, so the Doc is probably not link-shared: $name ($id)" >&2
    rm -f "$target"
    failed=1
    continue
  fi

  printf '%-34s %8s bytes\n' "$name" "$(wc -c < "$target" | tr -d ' ')"
done

exit "$failed"
