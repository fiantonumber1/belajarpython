#!/usr/bin/python3 
import os, sys
from PIL import Image

cwd = os.getcwd()
directory = "{}/images".format(cwd)
for infile in os.listdir(directory):
    try:
        full = "{}/{}".format(directory,infile)
        print(full)
        with Image.open(full) as im:
            if im.mode != 'RGB':
                im = im.convert('RGB')
            aas = im.rotate(-90).resize((128, 128), Image.ANTIALIAS)
            outfile = aas.save("/opt/icons/{}".format(cwd,infile),"JPEG")

    except:
        print("error")