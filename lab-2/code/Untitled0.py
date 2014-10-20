
# coding: utf-8

# In[56]:

import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt
import pybrain
from pybrain.structure import SigmoidLayer

from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle
import random
import math

### inline plotting
get_ipython().magic(u'matplotlib inline')

### Generate data
random.seed(1234)

n = 40
x = [random.gauss(0,1) for i in range(n)]
y = [random.gauss(0,1) for i in range(n)]
points = [[x[i], y[i]] for i in range(len(x))]

### Get normal quantiles
# radius1 = scipy.stats.norm.ppf(4.0/6)
# radius2 = scipy.stats.norm.ppf(5.0/6)
#print "Radius 1: %4.3f, radius 2: %4.3f" %(radius1, radius2)
radius1 = .87
radius2 = 1.45


### Put points into categories
for i in range(len(points)):
  modulus = math.sqrt(points[i][0]**2 + points[i][1]**2)
  if modulus < radius1:
    points[i].append(0)
  elif modulus < radius2:
    points[i].append(1)
  else:
    points[i].append(2)

# z is the list of categories
z = [points[i][2] for i in range(len(points))]

# xi, yi (i = 0, 1, 2) are lists of x and y coordinates of points in
# category i... this is ugly, but I couldn't find a way to plot
# with different color for each category
x0 = [value[0] for value in points if value[2]==0]
y0 = [value[1] for value in points if value[2]==0]
x1 = [value[0] for value in points if value[2]==1]
y1 = [value[1] for value in points if value[2]==1]
x2 = [value[0] for value in points if value[2]==2]
y2 = [value[1] for value in points if value[2]==2]

print "Length of 0: %d, of 1: %d, of 2: %d" %(len(x0), len(x1), len(x2))

plt.plot(x0, y0, "co")
plt.plot(x1, y1, "yo")
plt.plot(x2, y2, "go")
plt.show()

## training set
train= points[:int(0.7*len(points))]
test = points[int(0.7*len(points)):]


# In[57]:

## build network

net = buildNetwork(2, 2, 3, bias = True, outclass = SigmoidLayer)

print net

ds = SupervisedDataSet(2, 3)
for point in train:
  if point[2] == 0:
    ds.addSample( (point[0], point[1]), (1,0,0) )
  elif point[2] == 1:
    ds.addSample( (point[0], point[1]), (0,1,0) )
  else:
    ds.addSample( (point[0], point[1]), (0,0,1) )

trainer = BackpropTrainer(net, ds)
error = 10
iteration = 0
while error > 0.0001:
    error = trainer.train()
    iteration += 1
    print "Iteration: {0} Error {1}".format(iteration, error)

print "done"


# In[52]:

### testing on first 10 test cases
for i in range(10):
    predicted = net.activate((test[i][0], test[i][1]))
    print str(predicted), test[i][2]
    #print "True cateogory %d, predicted %d" %(test[i][2], predicted)


# In[53]:

### predictions
predictions = []
for point in test:
    print point
    prediction = net.activate((point[0], point[1]))
    print prediction
    predictions.append(np.argmax(prediction))
print predictions


# In[ ]:



