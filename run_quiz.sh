#!/usr/bin/env bash
# run_quiz.sh — launcher for the DMT MCQ Quiz GUI

# Resolve the directory this script lives in
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the Python quiz GUI, forwarding any arguments
python3 "$SCRIPT_DIR/dmt_mcq_quiz_gui.py" "$@"
