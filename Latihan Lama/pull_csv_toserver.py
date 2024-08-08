#!/usr/bin/env python3
import csv
import operator
import os
import re

pencacah_error = {}
pencacah_info = {}
pencacah_nama_error = {}
gabungan_info_error = {}
list_untuk_csv_1 = []
list_untuk_csv_2 = []


cwd = os.getcwd()
with open('{}/syslog.log'.format(cwd), "r") as totallog:
    for i in totallog:
        logbaru = totallog.readline().strip()
        if "ERROR" in logbaru:
            ambil2 = re.search(r'\(.*?\)', logbaru)
            error2 = ambil2.group(0).strip()
            nama2 = error2.strip("( )")
            if nama2 not in pencacah_nama_error:
                pencacah_nama_error[nama2] = 1
            else:
                pencacah_nama_error[nama2] += 1

            if "Ticket doesn't exist" in logbaru:
                error = "Ticket doesn't exist"
            else:
                ambil1 = re.search(r"(ERROR [\w \[]*) ", logbaru)
                error = ambil1.group(0).strip()
            error_without_error = re.sub("ERROR ","",error)
            if error_without_error not in pencacah_error:
                pencacah_error[error_without_error]=1
            else:
                pencacah_error[error_without_error]+=1
        elif "INFO" in logbaru:
            ambil1 = re.search(r'\(.*?\)', logbaru)
            error = ambil1.group(0).strip()
            nama = error.strip("( )")
            if nama not in pencacah_info:
                pencacah_info[nama] = 1
            else:
                pencacah_info[nama] += 1

for member,info in pencacah_info.items():
    if member not in gabungan_info_error:
       gabungan_info_error[member] = [0,0]
       gabungan_info_error[member][0] += info
    else:
        gabungan_info_error[member][0] += info

for membernya,kesalahan in pencacah_nama_error.items():
    if membernya not in gabungan_info_error:
       gabungan_info_error[membernya] = [0,0]
       gabungan_info_error[membernya][1] += kesalahan
    else:
        gabungan_info_error[membernya][1] += kesalahan

##### bikin csv list pertama
generator = sorted(pencacah_error.items(), key=operator.itemgetter(0))
fieldnames_1 = ["Error", "Count"]
for pemecah in generator:
    penyusun_1 = {}
    penyusun_1["Error"] = pemecah[0]
    penyusun_1["Count"] = pemecah[1]
    list_untuk_csv_1.append(penyusun_1)
with open('error_message.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames_1)
    writer.writeheader()
    writer.writerows(list_untuk_csv_1)

##### bikin csv list kedua
s = sorted(gabungan_info_error.items(), key=operator.itemgetter(0))
fieldnames = ["Username", "INFO", "ERROR"]
for pembuat in s:
    penyusun = {}
    penyusun["Username"] = pembuat[0]
    penyusun["INFO"] = pembuat[1][0]
    penyusun["ERROR"] = pembuat[1][1]
    list_untuk_csv_2.append(penyusun)

with open('user_statistics.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_untuk_csv_2)

