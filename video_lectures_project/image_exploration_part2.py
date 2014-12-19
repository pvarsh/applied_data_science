
# coding: utf-8

# In[1]:

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


####### Functions

# In[2]:

def initializeRectangle(ax):
    """ Initiealizes four empty lines and returns them in a list
        to be used to display bounding rectangle """
    return [ax.plot([],[],color = 'white', lw = 0.8, alpha = 0.7)[0] for i in range(4)]

def setLineData(lines, upperLeft, lowerRight):
    """ Takes a list of four lines
        and upperLeft and lowerRight points for a bounding rectangle
        sets data for lines to display bounding rectangle
    """
    #line1
    x1 = [upperLeft[0], lowerRight[0]]
    y1 = [upperLeft[1], upperLeft[1]]
    lines[0].set_data(x1, y1)
    #line2
    x2 = [lowerRight[0], lowerRight[0]]
    y2 = [upperLeft[1], lowerRight[1]]
    lines[1].set_data(x2, y2)
    #line3
    x3 = [lowerRight[0], upperLeft[0]]
    y3 = [lowerRight[1], lowerRight[1]]
    lines[2].set_data(x3, y3)
    #line4
    x4 = [upperLeft[0], upperLeft[0]]
    y4 = [lowerRight[1], upperLeft[1]]
    lines[3].set_data(x4, y4)

def histograms(img, fig, ax):
    #fig.subplots_adjust(0,0,1,1)
    #ax[0].axis('off')
    colors = ['red', 'green', 'blue']
    for i in range(3):
        ax[i].cla()
        ax[i].set_xlim((0,255))
        ax[i].hist(img[:,:,i].flatten(), bins = 256, facecolor = colors[i], lw = 0, normed = True)
    fig.canvas.draw()
    fig.show()

#infile = "images/ml.jpg"
dpath, fname = sys.argv[1:3]
infile = os.path.join(dpath, fname)
img = nd.imread(infile)


# In[4]:

### Plot image
nrow, ncol = img.shape[:2]
ysize = 10.
xsize = ysize * float(ncol)/float(nrow)

fig1, ax1 = plt.subplots(num = 1, figsize = [xsize, ysize])
#windowLine, = ax1.plot([], [], color = 'white')
lines = initializeRectangle(ax1)
#rect = Rectangle((-1, -1), 0, 0, facecolor = 'none')
#fig1Rect = ax1.add_patch(rect)
#rectPoints = [[10, 10], [40, 40], [10, 40], [40, 10]]
#rectPatch = plt.Polygon(rectPoints, facecolor = 'none')
#ax1.add_patch(rectPatch)
fig1.subplots_adjust(0, 0, 1, 1)
fig1.canvas.set_window_title('Mona Lisa')
ax1.imshow(img)
ax1.axis('off')
fig1.canvas.draw()
fig1.show()
    

### Plot histograms
fig2, ax2 = plt.subplots(num = 2, nrows = 3, ncols = 1)
fig2.canvas.set_window_title('Histograms')
histograms(img, fig2, ax2)


# In[5]:
# Get rectangles from image and update histograms
#rflag = True
#while rflag:
#    try:
#        upperLeft, lowerRight = [(int(round(i)), int(round(j))) for i, j in fig1.ginput(2, show_clicks = True)]
#        x = [upperLeft[0], lowerRight[0]]
#        y = [upperLeft[1], lowerRight[1]]
#        if x[0] == x[1] and y[0] == y[1]:
#            histograms(img, fig2, ax2)
#            for line in lines:
#                line.set_visible(False)
#        else:
#            setLineData(lines, upperLeft, lowerRight)
#            for line in lines:
#                line.set_visible(True)
#            histograms(img[upperLeft[1]:lowerRight[1], upperLeft[0]:lowerRight[0], :], fig2, ax2)
#        fig1.canvas.draw()
#    except:
#        rflag = False


# In[6]:
# Get values from histograms and update image
selectBands = []
tolerance = 5

rflag = True
while rflag:
    if len(selectBands) > 0:
        ### set existing bands to invisible (if any exist)
        ### this may be very inefficient if the invisible bands remain somewhere in figure or axis object and take up resources
        ### but it gets things done for the scope of the assignment
        [band.set_visible(False) for band in selectBands] # this may be inefficient since it doesn't remove old rectangles
    
    rgbPick = [(int(round(i))) for i, j in fig2.ginput(3, show_clicks = True)]
    if len(rgbPick) != 3: #break the loop if user pressed Escape
        break
        
    # create verical bands around selected values
    selectBands = [ax2[i].axvspan(rgbPick[i]-tolerance, rgbPick[i]+tolerance, facecolor = 'black', alpha = 0.4)                   for i in range(len(rgbPick))]
    fig2.canvas.draw()
    
    # create (or update) mask
    mask = np.ones(img.shape, dtype=np.float64)
    print "shape mask", mask.shape
    #index = (img[:,:,0] < rgbPick[0]-tolerance) or (img[:,:,0] > rgbPick[0]+tolerance)
    index = ((img[:,:,0] < (rgbPick[0]-tolerance)) | (img[:,:,0] > (rgbPick[0]+tolerance))) &\
            ((img[:,:,1] < (rgbPick[1]-tolerance)) | (img[:,:,1] > (rgbPick[1]+tolerance))) &\
            ((img[:,:,2] < (rgbPick[2]-tolerance)) | (img[:,:,2] > (rgbPick[2]+tolerance)))
    mask[index] = 0.25
    print "mask[index]141", mask.shape
    ax1.imshow((img*mask).clip(0,255).astype(np.uint8))
    fig1.canvas.draw()
        
    
    
