import os
import glob
from PIL import Image
from sys import argv
def changeType(img):
    im = Image.open(img)
    first = img.split(".")[0]
    im.save(first+".png")

def resize(img,height,width):
    im = Image.open(img).convert('LA')
    w,h = im.size
    newIm = im.resize((height,width))
    first = img.split(".")[0]
    newIm.save(first+"copy.png")

def jpegToPng():
    images = glob.glob("*.jpeg")
    for image in images:
        change(image)
    images = glob.glob("*.jpg")
    for image in images:
        changeType(image)

def resize(height,width):
    images = glob.glob("*.png")
    for image in images:
        resize(image,height,width)

height = argv[1]
width = argv[2]
