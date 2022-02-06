from PIL import Image
from numpy import asarray

def loadImgToArray(path: str):
    return imgToArray(loadImage(path))

def loadImage(path: str):
    return Image.open(path)
    
def imgToArray(img): 
    return asarray(img)

def read_file(filename):
    print(filename)
    with open(filename, 'r') as infile:
        text = infile.read()
    return text