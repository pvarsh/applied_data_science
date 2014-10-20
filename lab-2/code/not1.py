#learn XOR with a nerual network with saving of the learned paramaters

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

if __name__ == "__main__":
  ds = SupervisedDataSet(2, 1)
  ds.addSample( (0,0) , (1,))
  ds.addSample( (1,0) , (0,))

  net = buildNetwork(2, 4, 1, bias=True)

  trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
  trainer.trainOnDataset(ds, 3000)
  trainer.testOnData()

  print net.activate((1,0))
  print net.activate((1,0))
  print net.activate((0,0))
  print net.activate((0,0))

