from pybrain.datasets.supervised import SupervisedDataSet 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer

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

def print_f_list(flist, name = ""):
    print "\n### ", name
    for f, _ in flist:
        print f.split('/')[-1] 
 
if __name__ == "__main__":
    path_pos = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/my-face/resized/"
    path_neg = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/other_faces_resized/"
   
    # truth:positive
    true_val = 1
    false_val = -1
 
    # making training set of positive images
    files_pos = [(f, true_val) for f in glob.glob(path_pos + "*.png")]
    random.shuffle(files_pos)
    splt = int(len(files_pos) * 2.0/3)
    files_pos_train = files_pos[:splt]
    files_pos_test = files_pos[splt:]

    # making training set of negative images
    files_neg = [(f, false_val) for f in glob.glob(path_neg + "*.png")]
    random.shuffle(files_neg)
    splt = int(len(files_neg) * 2.0/3)
    files_neg_train = files_neg[:splt]
    files_neg_test = files_neg[splt:]
   
    print_f_list(files_neg_train, "files_neg_train")
    print_f_list(files_neg_test, "files_neg_test")
    print_f_list(files_neg, "files_neg")
 
    # putting together training and test sets
    train = files_pos_train + files_neg_train
    test = files_pos_test + files_neg_test
    random.shuffle(train)
    random.shuffle(test)
    
    # first image to start the training set
    f, truth = train.pop()
    t = loadImage(f)
    
    # build network
    net = buildNetwork(len(t), int(.05*len(t)), int(0.05*len(t)), 1)
   
    # initialize data set
    ds = SupervisedDataSet(len(t), 1)
    ds.addSample(t, truth)
    # add the rest of elements to data set
    for img, truth in train:
        print truth
        ds.addSample(loadImage(img), truth)
    

    # train the network
    trainer = BackpropTrainer(net, ds)
    error = 1 # was 10
    iteration = 0
    while error > 0.0001: # was 0.0001 
        error = trainer.train()
        iteration += 1
        print "Iteration: {0} Error {1}".format(iteration, error)
    
    for img, truth in test:
        print "Result (%d): %d" %(truth, net.activate(loadImage(img)))
   # print "\nResult (N): ", net.activate(loadImage('pic/face_4copy.png'))
   # print "\nResult (Y): ", net.activate(loadImage('pic/image_9copy.png'))
   # print "\nResult (Y): ", net.activate(loadImage('pic/image_10copy.png'))
   # print "\nResult (N): ", net.activate(loadImage('pic/face_3copy.png'))
   # print "\nResult (Y): ", net.activate(loadImage('pic/image_15copy.png'))
