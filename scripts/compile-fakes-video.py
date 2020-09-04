"""
Compile all of the fakes into a folder and make a video
"""

import glob2
import cv2
from progress.bar import Bar

fakes = sorted(glob2.glob("./results/**/fakes*[0-9].png"))

bar = Bar('Loading images', max=len(fakes))

images = []
for fake in fakes:
    img = cv2.imread(fake)
    height, width, layers = img.shape
    size = (width,height)
    images.append(img)
    bar.next()

bar.finish()

bar2 = Bar('Creating video', max=len(fakes))

out = cv2.VideoWriter('fakes.avi',cv2.VideoWriter_fourcc(*'XVID'), 12, size,1)
 
for i in range(len(images)):
    out.write(images[i])
    bar2.next()

bar2.finish()

out.release()

