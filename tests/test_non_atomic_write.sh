#!/bin/sh
# Proves internal/generate_readme.py's atomic_write() leaves the target file
# untouched when the writer process is killed mid-write.
set -e

WORKDIR=$(mktemp -d)
trap 'rm -rf "$WORKDIR"' EXIT

REPO_ROOT=$(cd "$(dirname "$0")/.." && pwd)
TARGET="$WORKDIR/README.md"
printf '%s' "ORIGINAL CONTENT" > "$TARGET"
BEFORE=$(wc -c < "$TARGET")

cat > "$WORKDIR/slow_write.py" <<PY
import sys
sys.path.insert(0, "$REPO_ROOT/internal")
from pathlib import Path
import generate_readme as g
import time

orig_replace = g.os.replace

def slow_replace(src, dst):
    time.sleep(2)
    return orig_replace(src, dst)

g.os.replace = slow_replace
g.atomic_write(Path("$TARGET"), "X" * 60000)
PY

python3 "$WORKDIR/slow_write.py" &
PID=$!
sleep 0.5
kill -9 "$PID"
wait "$PID" 2>/dev/null || true

AFTER=$(wc -c < "$TARGET")
AFTER_CONTENT=$(cat "$TARGET")

echo "before: $BEFORE bytes"
echo "after: $AFTER bytes"

if [ "$AFTER_CONTENT" != "ORIGINAL CONTENT" ]; then
  echo "FAIL: target file was modified/truncated by an interrupted write"
  exit 1
fi

echo "PASS: target file unchanged after interrupted write"
