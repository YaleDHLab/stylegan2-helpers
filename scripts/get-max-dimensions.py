import os
import glob
import cv2
from progress.bar import Bar

RAW_IMAGE_DIR = os.environ["RAW_IMAGE_DIR"]
RESIZE_DIR = os.environ["RESIZE_DIR"]
RAW_IMAGE_EXT = os.environ["RAW_IMAGE_EXT"]

print("Loaded config")
print(RAW_IMAGE_DIR)
print("resize_dir", RESIZE_DIR)
print(RAW_IMAGE_EXT)

img_glob = f'{RAW_IMAGE_DIR}/*.{RAW_IMAGE_EXT}'

files = glob.glob(img_glob)
bar = Bar('Processing', max=len(files))

max_dimensions = 0
max_h = 0
max_w = 0
max_c = 0
for fname in files:

    im = cv2.imread(fname)
    h, w, c = im.shape

    dimensions = h * w

    if dimensions > max_dimensions:
        print("\nnew largest image:", dimensions, h, w, c)
        max_dimensions = dimensions
        max_h = h
        max_w = w
        max_c = c


    bar.next()

bar.finish()

print("Largest dimension found: ", dimensions, h, w, c)

