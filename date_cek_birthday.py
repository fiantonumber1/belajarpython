#!/usr/bin/env python3


import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    print("not function")

def list_newer(start_date):
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    kalender = {}
    for row in reader:
        tester = datetime.datetime.strptime(row[3], '%Y-%m-%d').timestamp()
        if tester not in kalender:
            kalender[tester] = []
            kalender[tester].append("{} {}".format(row[0], row[1]))
        elif tester in kalender:
            kalender[tester].append(row[1])
    baru = sorted(kalender.items())
    kalender_baru = {}
    n = 0
    for i in baru:
        kalender_baru[n] = i
        n += 1
    if start_date <= datetime.datetime(2018, 1, 1):
        for tanggal, nama in kalender_baru.items():
            tanggal = datetime.datetime.fromtimestamp(nama[0])
            print("Started on {}: {}".format(tanggal.strftime("%b %d, %Y"), nama[1]))
    elif start_date > datetime.datetime.today():
        pass
    elif start_date < datetime.datetime.today():
        start_date_timestamp = start_date.timestamp()
        counting = 0
        for tanggal, nama in kalender_baru.items():
            if nama[0] >= start_date_timestamp:
                tanggal = datetime.datetime.fromtimestamp(nama[0])
                print("Started on {}: {}".format(tanggal.strftime("%b %d, %Y"), nama[1]))

def main():
    start_date = get_start_date()
    list_newer(start_date)


if __name__ == "__main__":
    main()



