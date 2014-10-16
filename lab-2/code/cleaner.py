import os
import glob
from PIL import Image
import ExifTags

def changeType(img):
    im = Image.open(img)
    first = img.split(".")[0]
    im.save(first+".png")

def resize(img, path_out = ""):
    im = Image.open(img).convert('LA')
    w,h = im.size
    newIm = im.resize((40,40))
    first = img.split(".")[0]
    newIm.save(path_out + first + "copy.png")

path_in = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/full_size/"
path_out = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-2/images/faces/resized/"

images = glob.glob(path_in + "*.jpg")

#for image in images:
#  im = Image.open(image)
#  for orientation in ExifTags.TAGS.keys():
#    print orientation  

for image in images:
  changeType(image)

images = glob.glob(path_in + "*.png")
for image in images:
    resize(image)
