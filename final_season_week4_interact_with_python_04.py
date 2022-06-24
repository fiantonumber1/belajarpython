#!/usr/bin/env python3
import reports
import os
import emails

cwd = os.getcwd()
datas = os.listdir('{}/supplier-data/descriptions'.format(cwd))
s = ["name","weight"]
dictionary = ''
for data in datas:
  filenya = "{}/supplier-data/descriptions/{}".format(cwd,data)
  with open(filenya,"r") as line:
    x = 0
    for lines in line:
        if x==0:
            m = "name: " + lines.rstrip('\n')
            dictionary += m
            dictionary += "<br/>"
        elif x==1:
            m = "weight: " + lines.rstrip('\n')
            dictionary += m
            dictionary += "<br/>"
        elif x==2:
            dictionary += "<br/>"
        x+=1

title = "Procesed update"
attachment = "/tmp/processed.pdf"
paragraph = "fian<br/>fian2<br/>fian3"
reports.generate_report(attachment, title, dictionary)
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject_line = "Upload Completed - Online Fruit Store"
email_body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
message = emails.generate(sender, receiver, subject_line, email_body, "/tmp/processed.pdf")

emails.send(message)
