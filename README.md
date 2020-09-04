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

Now you need to activate your virtual environment to use the rest of the scripts

```
. venv/bin/activate
```

You should see your prompt changed with `(venv)` added to it.

### resize-squares.py

You need squares images that n^2 in either dimension, meaning 1024x1024, for example. If your input images are not in this format, use resize-squares.py. This will take images from your `RAW_IMAGE_DIR` with the `RAW_IMAGE_EXT` file extension and create an `IMAGE_DIR` filled with 1024x1024 crops. 

If you already have these in this format and don't need to square your images, just manually set the `IMAGE_DIR` and don't run `resize-squares.py`.

This script requires the env vars set by config.sh, so you can run:

```bash 
bash config.sh ; python scripts/resize-squares.py
```

### create-datasets.sh

Creates the data sets from the data directory.

```
bash scripts/create-datasets.sh
```

This uses nohup, so you can safely disconnect your terminal session.

### train-on-data.sh

You'll want to delete the line:

```
    --resume-pkl="$LATEST_SNAPSHOT" \
```

when you first start. You'll want to add a line line this when you need to resume training, such as after a crash, but you'll need to point it to an appropriate file in your own results dir.

Usage:

```bash
bash scripts/train-on-data.sh
```

### compile-fakes-video.py

Turn the results fake pngs into a video using openCV2.

```bash
bash scripts/compile-fakes-video.py
```

This assumes your results are in ./results, which they should be by default.




