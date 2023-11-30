import os, glob
from PIL import Image

for infile in glob.glob('reduzir/*.jpg'):
    with Image.open(infile) as im:
        width = im.width // 2
        height = im.height // 2
        redefine = im.resize((width, height))
        redefine.save(infile, quality="high")