
# coding: utf-8

# ### Final project for image analysis module

# In[1]:

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


####### Problem 1

# In[2]:

img = mf((255 - nd.imread('images/ml.jpg')[::1,::2,::-1]).astype(float), (8, 2, 1)).clip(0,255).astype(np.uint8)
### Explanation:
### 1. nd.imread reaturns a 3D array
### 2. Then subsetting [::2, ::1, ::-1] inverses colors and skips every other column
### 3. 255 - ... converts to negative
### 4. .astype(float)
### 5. mf() applies median filter
### 6. .clip() clips
### 7. .astype(np.uint8) converts to uint

nrow, ncol = img.shape[:2]

ysize = 10.
xsize = ysize * float(ncol)/float(nrow)

fig1, ax1 = plt.subplots(num = 1, figsize = [xsize, ysize])
fig1.canvas.set_window_title('modiefied Mona Lisa')
fig1.subplots_adjust(0, 0, 1, 1)
ax1.axis('off')
im1 = ax1.imshow(img)
fig1.canvas.draw()
plt.show()


# In[ ]:



