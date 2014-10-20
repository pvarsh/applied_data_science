
# coding: utf-8

# In[12]:

#learn XOR with a nerual network with saving of the learned paramaters

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer
import pickle
import random
from matplotlib import pyplot as plt

if __name__ == "__main__":
  ds = SupervisedDataSet(2, 1)
  ds.addSample( (0,0) , (0,))
  ds.addSample( (0,1) , (1,))
  ds.addSample( (1,0) , (1,))
  ds.addSample( (1,1) , (0,))

  net = buildNetwork(2, 1, bias=True, outclass = SigmoidLayer)

  # try:
        #         f = open('_learned', 'r')
  #   net = pickle.load(f)
  #   f.close()
  # except:
  trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
  trainer.trainOnDataset(ds, 500)
  trainer.testOnData()
  # f = open('_learned', 'w')
  # pickle.dump(net, f)
  # f.close()
  

  print net.activate((1,1))
  print net.activate((1,0))
  print net.activate((0,1))
  print net.activate((0,0))

  testUnif = [(random.uniform(0,1), random.uniform(0,1)) for i in range(1000)]
  predictions = []
  for i in range(len(testUnif)):
    prediction = net.activate(testUnif[i])[0]
    predictions.append(prediction)

  #print predictions
  x = [pair[0] for pair in testUnif]
  y = [pair[1] for pair in testUnif]
  
  fig = plt.figure()
  plt.scatter(x,y, c = predictions)
  fig.savefig('xor.png', dpi = 300)
  


# In[12]:




# In[ ]:



