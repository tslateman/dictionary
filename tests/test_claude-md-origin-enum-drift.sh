#!/bin/sh
# Guards against CLAUDE.md drifting from the origin values internal/generate_readme.py accepts.
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE_MD="$ROOT/CLAUDE.md"
GENERATOR="$ROOT/internal/generate_readme.py"

RULE_LINE="$(grep -n 'Rules the generator enforces' "$CLAUDE_MD")"

ACCEPTED="$(grep -o 'if origin not in ([^)]*)' "$GENERATOR" | grep -o '"[a-z]*"' | tr -d '"')"

fail=0
for origin in $ACCEPTED; do
    case "$RULE_LINE" in
        *"$origin"*) ;;
        *)
            echo "FAIL: CLAUDE.md 'Rules the generator enforces' line omits origin value '$origin', which internal/generate_readme.py accepts" >&2
            fail=1
            ;;
    esac
done

if [ "$fail" -ne 0 ]; then
    exit 1
fi

echo "ok: CLAUDE.md rule line lists every origin value the generator accepts"
