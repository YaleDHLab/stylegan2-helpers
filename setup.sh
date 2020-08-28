#!/usr/bin/env bash

# Set up the environment.

# Stop if anything crashes
set -e

# Load ENV vars
. config.sh


# Set up a virtual environment
if [ -d "./venv" ]; then
    echo "+ Virtual env already exists."
else
    echo "* Setting up virtual env."
    python3 -m venv venv
fi

# Enter virtual env
# and install requirements
. ./venv/bin/activate &&
pip install -r requirements.txt

# Clone StyleGAN2 repo
if [ -d "./stylegan2" ]; then
    echo "+ StyleGAN2 folder found"
else
    echo "* Cloning StyleGAN2 repo"
    # Temporarily replacing official repo with ashirviskas repo,
    # which adds a resume training arguments required for restarting
    # git clone https://github.com/NVlabs/stylegan2.git
    git clone https://github.com/ashirviskas/stylegan2.git
fi

# Finished message
echo ""
echo ""
echo "Finished setting up!"
echo "Check out the docs for StyleGAN2 here: https://github.com/NVlabs/stylegan2"
echo ""
