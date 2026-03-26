#!/usr/bin/env bash
# CogniHire — local development launcher
# Usage: ./run.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Verify .env exists
if [ ! -f ".env" ]; then
    echo "ERROR: .env not found. Copy .env.example and fill in your MongoDB credentials."
    echo "  cp .env.example .env"
    exit 1
fi

echo "Starting CogniHire..."
python3.12 -m streamlit run apps/web/app.py \
    --server.headless false \
    --browser.gatherUsageStats false
