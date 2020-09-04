# Original code by Doug. I'm modifying to make square images. -Jake

from keras.preprocessing.image import load_img, img_to_array, array_to_img, save_img
import glob, os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import imsave
from multiprocessing import Pool, cpu_count
import io
from PIL import Image
import sys

RAW_IMAGE_DIR = os.environ["RAW_IMAGE_DIR"]
RESIZE_DIR = os.environ["RESIZE_DIR"]
RAW_IMAGE_EXT = os.environ["RAW_IMAGE_EXT"]

print("Loaded conifg")
print(RAW_IMAGE_DIR)
print("resize_dir", RESIZE_DIR)
print(RAW_IMAGE_EXT)

img_glob = f'{RAW_IMAGE_DIR}/*.{RAW_IMAGE_EXT}'

# nb:
# np uses h,w,c
# keras uses w,h,c

width = 1024
height = 1024
out_dir = f'{RESIZE_DIR}/' + '{}-{}-crops'.format(width, height)

if not os.path.exists(out_dir):
  os.makedirs(out_dir)

def clip(img, axis=-1):
  arr = img_to_array(img).squeeze()
  sums = np.sum(arr, axis=axis)
  if np.all(sums == 0):
    print('WARNING: empty image found')
    return img
  i = 0
  j = len(sums)-1
  while sums[i] == 0: i += 1
  while sums[j] == 0: j -= 1
  arr = arr[:, i:j] if axis == 0 else arr[i:j, :]
  return array_to_img(np.expand_dims(arr, axis=2))
  
def crop(img):
  img = clip(img, axis=0)
  img = clip(img, axis=-1)
  return img

total_images = len(glob.glob(img_glob))
done_images = 0
last_message = 0
def process_image(i):
  global done_images, last_message
  done_images += 1
  path = os.path.join(out_dir, '{}-{}-cropped-'.format(width, height) + os.path.basename(i))
  if os.path.exists(path): return
  j = load_img(i, color_mode='grayscale')
  # crop tightly to car pixels
  j = crop(j)
  # resize the cropped car to `width`w by `heihgt`h while keeping aspect ratio
  w, h = j.size
  scale = min(width/w, height/h)
  r = j.resize((int(w*scale), int(h*scale)))
  # center the resized car in the z vector
  arr = img_to_array(r).squeeze()
  h, w = arr.shape
  z = np.zeros((height, width))
  pad_top = (height-h)//2
  pad_side = (width-w)//2  
  # print(h, pad_top, w, pad_side)

  if done_images % 100 == 0 :
    total_done_images = len(os.listdir(out_dir))
    pct_done = total_done_images * 100 / total_images
    print(str(int(pct_done)) + r"% completed (" + str(total_done_images) + "/" + str(total_images) + ")")
  z[pad_top:pad_top+h, pad_side:pad_side+w] = arr
  
  # save the cropped image
  #imsave(path, z, cmap="gray")
  # Convert the image to a PIL object so we can remove the alpha channel
  buf = io.BytesIO()
  imsave(buf, z, cmap="gray")
  buf.seek(0)
  im = Image.open(buf)
  im.convert("RGB").save(path)
  
cpus_to_use = int(cpu_count() / 2)
print("Using " + str(cpus_to_use) + " cpus")
with Pool(cpus_to_use) as p:
    p.map(process_image, glob.glob(img_glob))
# for i in glob.glob(img_glob):
#    process_image(i)