####### Applied Urban Science 2014 Image/video module final
# Peter Varshavsky
#######

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf

### Problem 1

img = nd.imread('images/ml.jpg')

nrow, ncol = img.shape[:2]

xsize = 6.
ysize = xsize * float(nrow) / float(ncol)

fig0, ax0 = plt.subplots(num = 0, figsize = [xsize, ysize])
fig0.subplots_adjust(0, 0, 1, 1)
ax0.axis('off')
im0 = ax0.imshow(img)
fig0.canvas.draw()
plt.show()
