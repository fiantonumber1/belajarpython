#! /usr/bin/env python3
import os
import requests

cwd = os.getcwd()
datas = os.listdir('{}/supplier-data/descriptions'.format(cwd))
s = ["name","weight","description","image_name"]
count = 0
for data in datas:
  count += 1
  dictionary = {}
  filenya = "{}/supplier-data/descriptions/{}".format(cwd,data)
  with open(filenya,"r") as line:
    x = 0
    for lines in line:
        if x == 1:
          m = lines.rstrip('\n')
          counting = len(m)-4
          dictionary[s[x]]=int(m[:counting])
        else:
          dictionary[s[x]] = lines.rstrip('\n')
        x+=1
  if count != 10:
    data = "00{}.jpeg".format(count)
  else:
    data = "010.jpeg".format(count)
  dictionary[s[3]] = data
  ip_address = "34.133.39.96"
  upload = requests.post('http://{}/fruits/'.format(ip_address), json=dictionary)
  print('Response', upload.status_code)
  if not upload.status_code == 201:
      print('There is problem in run')
