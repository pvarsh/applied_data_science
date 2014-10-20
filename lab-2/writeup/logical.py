#learn boolean operators with a nerual network with saving of the learned paramaters

import sys
import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def buildAndTrain(ds):
  net = buildNetwork(2, 4, 1, bias=True)
  trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
  trainer.trainOnDataset(ds, 1000)
  return net

def main(argv):
  operator = argv[0]
  ds = SupervisedDataSet(2, 1)
  if operator == 'and':
    ds.addSample( (0,0) , (0,))
    ds.addSample( (0,1) , (0,))
    ds.addSample( (1,0) , (0,))
    ds.addSample( (1,1) , (1,))
    correct = [1, 0, 0, 0]
  elif operator == 'or':
    ds.addSample( (0,0) , (0,))
    ds.addSample( (0,1) , (1,))
    ds.addSample( (1,0) , (1,))
    ds.addSample( (1,1) , (1,))
    correct = [1, 1, 1, 0]
  elif operator == 'nor':
    ds.addSample( (0,0) , (1,))
    ds.addSample( (0,1) , (0,))
    ds.addSample( (1,0) , (0,))
    ds.addSample( (1,1) , (0,))
    correct = [0, 0, 0, 1]
  elif operator == 'not':
    ds.addSample( (0,0) , (1,))
    ds.addSample( (0,1) , (1,))
    ds.addSample( (1,0) , (0,))
    ds.addSample( (1,1) , (0,))
    correct = [0, 0, 1, 1]
    
  ntrials = int(argv[1])
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
    if len(argv) == 3 and argv[2] == "true":
      for r in result:
        print "%7.6f" %r
  
  errors = []
  counter = 0
  for result in results:
    counter += 1
    error = sum([(result[i] - correct[i])**2 for i in range(len(points))])
    if error >= 0.1:
      print "Iteration %d" %counter
      print "Error %7.6f" %error
      for r in result:
        print "%7.6f" %r

if __name__ == "__main__":
  if len(sys.argv) >= 3:
    main(sys.argv[1:])
  else:
    print "Incorrect number of parameters"
