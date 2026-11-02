#!/bin/sh
# Veröffentlicht den aktuellen Stand des Arbeits-Branches auf gh-pages (GitHub Pages).
# Interne Design-Arbeitsdateien (.impeccable/) werden dabei nicht mitveröffentlicht.
set -e
cd "$(dirname "$0")/.."
BRANCH=$(git rev-parse --abbrev-ref HEAD)
git fetch -q origin gh-pages || true
IDX=$(mktemp)
GIT_INDEX_FILE="$IDX" git read-tree HEAD
GIT_INDEX_FILE="$IDX" git rm -r -q --cached --ignore-unmatch .impeccable
TREE=$(GIT_INDEX_FILE="$IDX" git write-tree)
rm -f "$IDX"
PARENT=$(git rev-parse -q --verify origin/gh-pages || true)
MSG="Veröffentlichung von $BRANCH ($(git rev-parse --short HEAD))"
if [ -n "$PARENT" ]; then C=$(git commit-tree "$TREE" -p "$PARENT" -m "$MSG"); else C=$(git commit-tree "$TREE" -m "$MSG"); fi
git push origin "$C:refs/heads/gh-pages"
echo "gh-pages -> $C"
