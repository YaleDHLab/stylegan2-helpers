#!/usr/bin/env bash

echo "Loading configuration..."

# Update below with path to your files

# The source images cropped square (eg. 1024x1024)
export RAW_IMAGE_DIR=/home/dhlab/faces/Datasets/Photogrammar-FaceNet/fsa_faces_cropped
export RAW_IMAGE_EXT="jpg"
export RESIZE_DIR=/home/dhlab/faces/Datasets/Photogrammar-FaceNet/fsa_faces_resized
export IMAGE_DIR=$RESIZE_DIR/1024-1024-crops

# These you don't need to touch. These scripts are meant to be run 
# from the repository root directory. The datasets will be in a 
# subdirectory of $DATA_DIR named "datasets"
export DATA_DIR="$(pwd)"