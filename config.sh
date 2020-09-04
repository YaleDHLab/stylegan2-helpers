#!/usr/bin/env bash

echo "Loading configuration..."

# Update below with path to your files

#######################################
# Image pre-processing
#######################################

# Note: if you already have 1024-1024 images
# you can ignore the top three variables (or
# comment them out) and just set IMAGE_DIR

export RAW_IMAGE_DIR=/home/dhlab/faces/Datasets/Photogrammar-FaceNet/fsa_faces_cropped
export RAW_IMAGE_EXT="jpg"
export RESIZE_DIR=/home/dhlab/faces/Datasets/Photogrammar-FaceNet/fsa_faces_resized

# This is where your images lives that are ready 
# for turning into data sets 
export IMAGE_DIR=$RESIZE_DIR/1024-1024-crops


#######################################
# You can probably ignore from here down
#######################################

# These you don't need to touch. These scripts are 
# meant to be run from the repository root directory. 
# The datasets will be in a subdirectory of $DATA_DIR 
# named "datasets"
export DATA_DIR="$(pwd)"