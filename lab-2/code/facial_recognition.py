from pybrain.datasets.supervised import SupervisedDataSet 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import cv2
import glob
import os
import random

 
def loadImage(path):
    im = cv2.imread(path)
    return flatten(im)
 
def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result
 
if __name__ == "__main__":
    path_pos = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/resized-not-centered/"
    path_neg = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/not-my-face/"
    
    # making training set of positive images
    files_pos = [f, -1 for f in glob.glob(path_pos + "pv*.png")]
    random.shuffle(files_pos)
    splt = int(len(files_pos) * 2.0/3)
    files_pos_train = files_pos[:splt]
    files_pos_test = files_pos[splt:]

    # making training set of negative images
    files_neg = [f, -1 for f in glob.glob(path_neg + "*.png")]
    random.shuffle(files_neg)
    splt = int(len(files_neg) * 2.0/3)
    files_neg_train = files_neg[:splt]
    files_neg_test = files_neg[splt:]
    
    # putting together training and test sets
    train = random.shuffle(files_pos_train + files_neg_train)
    test = random.shuffle(files_pos_test + files_neg_test)

    # first image to start the training set 
    t, truth = loadImage(train[0])
    # build network
    net = buildNetwork(len(t), int(.03*len(t)), 1)
   
    # initialize data set 
    ds = SupervisedDataSet(len(t), truth)
    # add the rest of elements to data set
    for img, truth in train[1:]:
        ds.addSample(loadImage(img), truth)

    # train the network
    trainer = BackpropTrainer(net, ds)
    error = 10
    iteration = 0
    while error > 0.0001: 
        error = trainer.train()
        iteration += 1
        print "Iteration: {0} Error {1}".format(iteration, error)
    
    for img, truth in test:
        print "Result (%d): %d" %(truth, net.activate(loadImage(img))
   # print "\nResult (N): ", net.activate(loadImage('pic/face_4copy.png'))
   # print "\nResult (Y): ", net.activate(loadImage('pic/image_9copy.png'))
   # print "\nResult (Y): ", net.activate(loadImage('pic/image_10copy.png'))
   # print "\nResult (N): ", net.activate(loadImage('pic/face_3copy.png'))
   # print "\nResult (Y): ", net.activate(loadImage('pic/image_15copy.png'))
