import os
import glob
from PIL import Image
import ExifTags



def changeType(img):
    im = Image.open(img)
    first = img.split(".")[0]
    im.save(first+".png")

def resize(img, path_out = ""):
    #print 'a'
    im = Image.open(img).convert('LA')
    w,h = im.size
    newIm = im.resize((40,40))
    first = img.split(".")[-2].split("/")[-1]
    #print '\naaaa: ', first
    #print '\n'
    newIm.save(path_out + first + ".png")


### alligator 
print "########\n alligator \n##########"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/alligator/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/alligator_proc/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
for image in images:
    print image
    resize(image, path_out)



### cat 
print "########\n cat \n##########"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/cat/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/cat_proc/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
for image in images:
    print image
    resize(image, path_out)



### dog
print "########\n dog \n##########"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/dog/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/dog_proc/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
for image in images:
    print image
    resize(image, path_out)


### gorilla
print "########\n gorilla \n##########"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/gorilla/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/gorilla_proc/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
for image in images:
    print image
    resize(image, path_out)

### giraffe 
print "########\n giraffe \n##########"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/giraffe/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/animals/giraffe_proc/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
for image in images:
    print image
    resize(image, path_out)

