
#!/usr/bin/env python3

from multiprocessing import Pool
import os
import subprocess

cwd = os.getcwd()
src = "{}/data/prod".format(cwd)
directory = next(os.walk(src))[1]

def testing(directory):
    position= "{}/data/prod_backup".format(cwd)
    subprocess.call(["rsync", "-arq", src+'/'+ str(directory), position])

p = Pool(len(directory))
p.map(testing, directory)
