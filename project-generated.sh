#!/usr/bin/env bash

set -e 

LATEST_SNAPSHOT=$(python latest-snapshot.py)

echo "Using snapshot: $LATEST_SNAPSHOT"

python stylegan2/run_projector.py project-generated-images \
    --network="$LATEST_SNAPSHOT"
    --seeds=1 \
    --result-dir=./projections