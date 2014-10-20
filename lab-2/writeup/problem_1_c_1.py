#learn (A and B) or C with a nerual network with saving of the learned paramaters

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

if __name__ == "__main__":
  ds = SupervisedDataSet(3, 1)
  ds.addSample( (1,1,1) , (1,))
  ds.addSample( (1,1,0) , (1,))
  ds.addSample( (1,0,1) , (1,))
  ds.addSample( (0,1,1) , (1,))
  ds.addSample( (1,0,0) , (0,))
  ds.addSample( (0,1,0) , (0,))
  ds.addSample( (0,0,1) , (1,))
  ds.addSample( (0,0,0) , (0,))

  net = buildNetwork(3, 4, 1, bias=True)

  # try:
        #         f = open('_learned', 'r')
  #   net = pickle.load(f)
  #   f.close()
  # except:
  trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
  trainer.trainOnDataset(ds, 3000)
  trainer.testOnData()
  # f = open('_learned', 'w')
  # pickle.dump(net, f)
  # f.close()
  
  abc = [(1,1,1),
         (1,1,0),
         (1,0,1),
         (0,1,1),
         (1,0,0),
         (0,1,0),
         (0,0,1),
         (0,0,0)]
  
  for triple in abc:
    print triple, net.activate(triple)

