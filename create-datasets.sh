#!/usr/bin/env bash

# Exit if anything fails
set -e

# Load common vars
. config.sh

echo "* Running StyleGAN2:dataset.py"
echo "*     Image dir: $IMAGE_DIR"
echo "*      Data dir: $DATA_DIR"
python stylegan2/dataset_tool.py create_from_images "$DATA_DIR" "$IMAGE_DIR"