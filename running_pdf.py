






#!/usr/bin/env python3
import emails
import os
import reports
import ast
import re

table_data=[
  ['ID', 'Car', 'Price','Total Sales'],
  ['elderberries', 10, 0.45,""],
]


cwd = os.getcwd()
with open('{}/json.txt'.format(cwd), "r") as totallog:
    jumlah_baris=0
    for i in totallog:
         jumlah_baris+=1

def transform_to_(m):
    print(m)
with open('{}/json.txt'.format(cwd), "r") as totallog:
    baris=0
    for i in totallog:
         baris += 1
         if baris ==1:
             print(i.strip()[1:][:(len(i)-3)])
         elif baris==jumlah_baris:
             print(i.strip()[:(len(i)-2)])
         else:
             print(i.strip()[:(len(i)-2)])

description= ''
#reports.generate("/tmp/report.pdf", "Sales summary for last month", "{}".format(description), table_data)
#sender = "automation@example.com"
#receiver = "{}@example.com".format(os.environ.get('USER'))
#subject = "List of Fruits"
#body = "Hi\n\nI'm sending an attachment with all my fruit."
#message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
#emails.send(message)