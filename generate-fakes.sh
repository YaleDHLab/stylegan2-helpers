#!/usr/bin/env bash

set -e 

LATEST_SNAPSHOT=$(python latest-snapshot.py)

echo "Using snapshot: $LATEST_SNAPSHOT"

python stylegan2/run_generator.py generate-images \
    --network="$LATEST_SNAPSHOT" \
    --result-dir=./generator-results \
    --seeds=66,230,389,1518