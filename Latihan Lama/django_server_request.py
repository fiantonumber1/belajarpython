

#! /usr/bin/env python3
import os
import requests

datas = os.listdir('/data/feedback')
s = ["title","name","date","feedback"]
for data in datas:
  dictionary = {}
  with open("/data/feedback/"+"/"+data,"r") as line:
    x = 0
    for lines in line:
        dictionary[s[x]] = lines.rstrip('\n')
        x+=1
  print(lines[0])
  upload = requests.post(r'http://35.238.15.122/feedback/', json=dictionary)
  print('Response', upload.status_code)
  if not upload.status_code == 201:
      print('There is problem in run')
