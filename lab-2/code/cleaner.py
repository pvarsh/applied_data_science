import os
import glob
from PIL import Image
import ExifTags

print 'aaa'


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
    newIm.save(path_out + first + "copy.png")

#path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/full_size/"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/my-face/cropped/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/my-face/resized/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
print images
for image in images:
    print image
    resize(image, path_out)


### NOT MY FACE
print "########\n###########\n##########"
path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/other_faces/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/other_faces_resized/"

images = glob.glob(path_in + "*.jpg")
images = images + glob.glob(path_in + "*.JPG")
images = images + glob.glob(path_in + "*.png")
print images
for image in images:
    print image
    resize(image, path_out)

#for image in images:
#  im = Image.open(image)
#  for orientation in ExifTags.TAGS.keys():
#    print orientation  

#for image in images:
#  changeType(image)
#
#images = glob.glob(path_in + "*.png")
#for image in images:
#    resize(image)
