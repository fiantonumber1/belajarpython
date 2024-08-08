#!/usr/bin/python3
import os, sys
from PIL import Image

cwd = os.getcwd()
directory = "{}/supplier-data/images".format(cwd)
for infile in os.listdir(directory):
    try:
       filenya = "{}/{}".format(directory,infile)
       with Image.open(filenya) as im:
            rgb_image = im.convert('RGB')
            change_resize =rgb_image.resize((600, 400))
            hitungan = len(infile)-4
            change_resize.save("{}/{}jpeg".format(directory,infile[:hitungan]),"JPEG")
    except:
        print("cannot convert", infile)




