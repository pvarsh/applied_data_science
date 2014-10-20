import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle
import random
import math
#from enthought import chaco

random.seed(1234)

n = 100
x = [random.uniform(-1,1) for i in range(n)]
y = [random.uniform(-1,1) for i in range(n)]

points = [[x[i], y[i]] for i in range(len(x))]

for i in range(len(points)):
  modulus = math.sqrt(points[i][0]**2 + points[i][1]**2)
  if modulus < 0.3:
    points[i].append(0)
  elif modulus < 0.6:
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

plt.plot(x0, y0, "co")
plt.plot(x1, y1, "yo")
plt.plot(x2, y2, "go")
plt.show()

## training set
train= points[:int(0.7*len(points))]
test = points[int(0.7*len(points)):]

## build network

net = buildNetwork(2, 2, 3, bias = True)
ds = SupervisedDataSet(2, 3)
for point in train:
  if point[2] == 0:
    ds.addSample( (point[0], point[1]), (1,0,0) )
  elif point[2] == 1:
    ds.addSample( (point[0], point[1]), (0,1,0) )
  else:
    ds.addSample( (point[0], point[1]), (0,0,1) )

trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
trainer.trainOnDataset(ds, 1000)


print "done"
