from pybrain.datasets.supervised import SupervisedDataSet 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import cv2
 
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
 
    t = loadImage('pic/face_2copy.png')
    

    net = buildNetwork(len(t), .03*len(t), 1)
    ds = SupervisedDataSet(len(t), 1)
    ds.addSample(loadImage('pic/face_2copy.png'),(10,))
    ds.addSample(loadImage('pic/image_1copy.png'),(-10,))
    ds.addSample(loadImage('pic/image_2copy.png'),(-10,))
    ds.addSample(loadImage('pic/face_5copy.png'),(10,))
 
    trainer = BackpropTrainer(net, ds)
    error = 10
    iteration = 0
    while error > 0.0001: 
        error = trainer.train()
        iteration += 1
        print "Iteration: {0} Error {1}".format(iteration, error)
 
    print "\nResult (N): ", net.activate(loadImage('pic/face_4copy.png'))
    print "\nResult (Y): ", net.activate(loadImage('pic/image_9copy.png'))
    print "\nResult (Y): ", net.activate(loadImage('pic/image_10copy.png'))
    print "\nResult (N): ", net.activate(loadImage('pic/face_3copy.png'))
    print "\nResult (Y): ", net.activate(loadImage('pic/image_15copy.png'))
