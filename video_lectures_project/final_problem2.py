
# coding: utf-8

# In[1]:

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


# In[2]:

### 

#infile = "images/ml.jpg"
dpath, fname = sys.argv[1:3]
infile = os.path.join(dpath, fname)
img = nd.imread(infile)


# In[13]:

### Plot image

fig1, ax1 = plt.subplots(num = 1)
fig1.subplots_adjust(0,0,1,1)
fig1.canvas.set_window_title('Mona Lisa')
ax1.imshow(img)
ax1.axis('off')
fig1.canvas.draw()
#plt.show()

### Plot histograms
fig2, ax2 = plt.subplots(num = 2, nrows = 3, ncols = 1)
#fig2.subplots_adjust(0,0,1,1)

for i in range(3):
    ax2[i].set_xlim((0,255))
    
ax2[0].hist(img[:,:,0].flatten(), bins = 256, facecolor = 'red') 
ax2[1].hist(img[:,:,1].flatten(), bins = 256, facecolor = 'green')
ax2[2].hist(img[:,:,2].flatten(), bins = 256, facecolor = 'blue')


#np.log10(np.abs(1.0*imgs - mimg).max(-1).flatten()+1.0), bins=255)

ax2[0].axis('off')
fig2.canvas.draw()
plt.show()


# In[7]:




# In[12]:

img.mean(1).shape


# In[9]:



# In[ ]:



