
# coding: utf-8

# In[2]:

import os
import sys
import time
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt


##### Load all digits in single image

# In[3]:

img = nd.imread('images/digits.png')
nrow, ncol = img.shape[0:2]

##### Reshape and compute averages of each digit

# In[4]:

nums = img.reshape(50,20,100,20).transpose(0,2,1,3).reshape(5000,20,20)
nums_avg = np.array([nums[i*500:(i+1)*500].mean(0) for i in range(10)])


####### Regressing all numbers on averages

# In[5]:

PT = nums_avg.reshape(10,400)
P  = PT.transpose()
PTPinv = np.linalg.inv(np.dot(PT,P))

PTyys = [[np.dot(PT, nums[im].flatten()) for im in range(i*500, (i+1)*500)] for i in range(10)]
avecs = [[np.dot(PTPinv, PTy) for PTy in PTyys[i]] for i in range(10)]
avecsAll = np.array(avecs)

####### Plotting histograms

# In[131]:

#fig, ax = plt.subplots(num = 0, figsize = (24,16), nrows = 10, ncols = 10, sharex = True)
#fig.clf()
#fig, ax = plt.subplots(num = 0, figsize = (24,16), nrows = 10, ncols = 10, sharex = True)
#for i in range(10):
#    for j in range(10):
#        ax[j][i].cla()
#        ax[j][i].set_xlim(-2,2)
#        ax[j][i].hist(avecsAll[i, : , j], bins = 10, normed = True)
##         if i != 0:
##             ax[j][i].set_yticklabels([])
##         else:
##             ax[j][i].set_yticks([0, .5, 1, 1.5, 2, 2.5])
##             ax[j][i].set_yticklabels([0, .5, 1, 1.5, 2, 2.5], fontsize = 8)
#        if j != 9:
#            ax[j][i].set_xticklabels([])
#        else:
#            ax[j][i].set_xticks([-1.8, 0, 1.8])
#            ax[j][i].set_xticklabels([-1.8,0,1.8], fontsize = 8)
#        ax[j][i].tick_params(axis='y', which='major', labelsize=8)
#fig.subplots_adjust(hspace=0)
#fig.canvas.draw()
#fig.show()

figures = []
for i in range(10):
    fig, ax = plt.subplots(num = i, figsize = (6, 12), nrows = 10, sharex = True)
    fig.suptitle('Distribution of regression coefficients for ' + str(i))
    for j in range(10):
        ax[j].cla()
        ax[j].set_xlim(-2.5,2.5)
        ax[j].hist(avecsAll[i,:,j], bins = 10, normed = True)
        ax[j].tick_params(axis = 'y', which = 'major', labelsize = 8)
        ax[j].set_yticklabels([])
        ax[j].set_ylabel(j)
        if j != 9:
            ax[j].set_xticklabels([])
    fig.canvas.set_window_title('Histograms for ' + str(i) + ' digit') 
    figures.append((fig, ax))
    
[fig[0].show() for fig in figures]


#### Part 2. Error reports

# In[5]:

bins = np.arange(11)-0.5
hists = [np.array(np.histogram(np.argmax(avecsAll[i,:,:], axis = 1), bins = bins)[0]) for i in range(10)]
successRate = [hists[i][i]/500. for i in range(10)]
errorRate = [1 - s for s in successRate]
commonError = [np.argpartition(a = hists[i], kth = -2)[-2:-1][0] for i in range(10)]


# In[6]:
# Printing accuracy, no intercept
print "   Accuracy for model fit without intercept"
for i in range(10):
    print("{0}% of {1}s were incorrectly identified,".format(round(errorRate[i]*100,3), i) +\
    "the most common guess for those failures was {0}".format(commonError[i]))


#### Part 3. Animation

######## Misclassified 1s
#
## In[7]:
#
#errors = []
#classifiedAs = []
#
#for i, bad in enumerate(list(np.argmax(avecsAll[1], axis = 1) != 1)):
#    #print truth, i, argmax(avecsAll[1], axis = 1)[i]
#    if bad:
#        errors.append(i)
#        classifiedAs.append(np.argmax(avecsAll[1], axis = 1)[i])
#classedAs = np.argmax(avecsAll[1], axis = 1)[np.argmax(avecsAll[1], axis = 1) != 1]
#
#fig1, ax1 = plt.subplots(num=1,figsize=[4,4])
#fig1.subplots_adjust(0,0,1,1)
#ax1.axis('off')
#im1 = ax1.imshow(nums[0])
#t1 = ax1.text(2, 2, "", fontsize=12, color = 'white')
#
#fig1.canvas.draw()
#
#for i in range(len(errors)):
#    im1.set_data(nums[500+errors[i]])
#    t1.set_visible(False)
#    t1 = ax1.text(2, 2, classifiedAs[i], fontsize=12, color = 'white')
#    fig1.canvas.draw()
#    time.sleep(1)


####### Misclassified random 30-second animation

# In[41]:

badPredictions = np.array([(np.argmax(avecsAll[i], axis = 1) != i) for i in range(10)]).flatten()
classifications = np.array([np.argmax(avecsAll[i], axis = 1).flatten() for i in range(10)]).flatten()
index = np.arange(5000)
whereBad = index[badPredictions]

#fig1, ax1 = plt.subplots(num=1,figsize=[4,4])
#fig1.subplots_adjust(0,0,1,1)
#fig1.canvas.set_window_title('Misclassified 1s')
#ax1.axis('off')
#im1 = ax1.imshow(nums[0])
#t1 = ax1.text(2, 2, "", fontsize=12, color = 'white')

# In[68]:

np.random.shuffle(whereBad)
fig2, ax2 = plt.subplots(num = 11, figsize = [4,4])
fig2.subplots_adjust(0,0,1,1)
fig2.canvas.set_window_title('Misclassified')
ax2.axis('off')
im2 = ax2.imshow(nums[whereBad[0]])
t2 = ax2.text(.5,1.5, "Classified as: " + str(classifications[whereBad[0]]), fontsize = 12, color = 'white')
#fig1.canvas.draw()
fig2.show()
#fig1.show()

t0 = time.time()
dt = 0
i = 1
while dt < 15:
    im2.set_data(nums[whereBad[i]])
    t2.set_visible(False)
    t2 = ax2.text(.5,1.5, "Classified as: " + str(classifications[whereBad[i]]), fontsize = 12, color = 'white')
    time.sleep(.8)
    dt = time.time() - t0
    i += 1
    fig2.canvas.draw()


#### Part 4. Regression with intercept

# In[15]:

PT = nums_avg.reshape(10,400)
PT.shape


# In[11]:

PT = nums_avg.reshape(10,400)
PT = np.column_stack((PT, np.ones(10)))

#print "PT.shape", PT.shape
P  = PT.transpose()
#print "P.shape", P.shape
PTPinv = np.linalg.inv(np.dot(PT,P))
#print "PTPinv.shape", PTPinv.shape
#print nums[10].flatten().shape
PTyys = [[np.dot(PT, np.insert(nums[im].flatten(), 400, 1)) for im in range(i*500, (i+1)*500)] for i in range(10)]
avecs = [[np.dot(PTPinv, PTy) for PTy in PTyys[i]] for i in range(10)]
avecsAll = np.array(avecs)
#print avecsAll.shape


# In[12]:

aa = np.array([1,2,3,4,5])
#print np.insert(aa, 5, 6)


# In[13]:

bins = np.arange(11)-0.5
hists = [np.array(np.histogram(np.argmax(avecsAll[i,:,:], axis = 1), bins = bins)[0]) for i in range(10)]
successRate = [hists[i][i]/500. for i in range(10)]
errorRate = [1 - s for s in successRate]
commonError = [np.argpartition(a = hists[i], kth = -2)[-2:-1][0] for i in range(10)]


# In[14]:
# Printing accuracy wit with intercept
print "   Accuracy for model fit with intercept"
for i in range(10):
    print("{0}% of {1}s were incorrectly identified,".format(round(errorRate[i]*100,3), i) +\
    "the most common guess for those failures was {0}".format(commonError[i]))


# In[14]:




# In[ ]:



