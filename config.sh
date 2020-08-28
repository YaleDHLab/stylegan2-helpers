#!/usr/bin/env bash

echo "Loading configuration..."

# Update below with path to your files

# The source images cropped square (eg. 1024x1024)
IMAGE_DIR=/home/dhlab/EveryPixel/2020\ Data/resized/1024-1024-crops

# These you don't need to touch. These scripts are meant to be run 
# from the repository root directory. The datasets will be in a 
# subdirectory of $DATA_DIR named "datasets"
DATA_DIR="$(pwd)"