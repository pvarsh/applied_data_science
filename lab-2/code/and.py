#learn XOR with a nerual network with saving of the learned paramaters

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def buildAndTrain(ds):
  
  net = buildNetwork(2, 4, 1, bias=True)

  # try:
        #         f = open('_learned', 'r')
  #   net = pickle.load(f)
  #   f.close()
  # except:
  trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
  trainer.trainOnDataset(ds, 1000)
  trainer.testOnData()
  return net

if __name__ == "__main__":
  ds = SupervisedDataSet(2, 1)
  ds.addSample( (0,0) , (0,))
  ds.addSample( (0,1) , (0,))
  ds.addSample( (1,0) , (0,))
  ds.addSample( (1,1) , (1,))
 
  ntrials = 100 
  results = []
  counter = 0
  for i in range(ntrials):
    net = buildAndTrain(ds)
    points = [(1,1), (1,0), (0,1), (0,0)]
    result = [net.activate(point)[0] for point in points]
    results.append(result)
    #print result
    counter += 1
    print counter, " of ", ntrials
  
  AND = [1, 0, 0, 0]
  errors = []
  counter = 0
  for result in results:
    counter += 1
    error = sum([(result[i] - AND[i])**2 for i in range(4)])
    if error >= 0.1:
      print "Iteration %d" %counter
      print "Error %7.6f" %error
      for r in result:
        print "%7.6f" %r
