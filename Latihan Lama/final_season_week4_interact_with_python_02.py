#!/usr/bin/env python3
import os

import requests

cwd = os.getcwd()
directory = "{}/supplier-data/images".format(cwd)
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for infile in os.listdir(directory):
    filenya = "{}/{}".format(directory, infile)
    with open(filenya , 'rb') as opened:
        r = requests.post(url, files={'file': opened})
