#!/bin/ash

set -o errexit
set -o pipefail
set -o nounset

echo 'Starting API server...'
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
