# Faking images with stylegan2

> Scripts for faking images with with [stylegan2](https://github.com/NVlabs/stylegan2)

## Overview

These scripts are meant to automate the process of setting up an environment and making fake images from a corpus of input images on a machine with a discrete GPU. Since this is a long-running task, these scripts make it easy to start and then restart whenever the process stops for one reason or another, such as a power outage, system or program crash.

## Scripts

These scripts won't work off the bat, but they document the process I went through to get this environment working on an ubuntu system with a discrete GPU.

**NOTE: These scripts have hard coded file paths, so they need to be modified to work. Consider this your warning; I won't repeat in in each section below.**

### config.sh

Start here. You'll want to set some variables here that point to your files. However, not all of the scripts use these vars, and a nice improvement to this repo would be to replace hardcoded paths to pull these from the env vars set in this file.

### setup.sh

Start here. This script sets up a Python virtual env and installs requirements.txt, and it clones a copy of StyleGAN 2. Currently we are using this [modified fork](https://github.com/ashirviskas/stylegan2.git) that adds features to resume training. 

### create-datasets.sh

Creates the data sets from the data directory.

### train-on-data.sh

You'll want to delete the line:

```
    --resume-pkl="results/00016-stylegan2-datasets-1gpu-config-f/network-snapshot-001065.pkl" \
```

when you first start. You'll want to add a line line this when you need to resume training, such as after a crash, but you'll need to point it to an appropriate file in your own results dir.

### compile-fakes-video.py

Turn the results fake pngs into a video using openCV2.

### resize-squares.py

This was just a quick script I wrote to modify the original source images I received. This is very specific to the data and mostly remains as a reminder to myself.





