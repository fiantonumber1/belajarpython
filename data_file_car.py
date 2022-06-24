#!/usr/bin/env python3
import os
import report1
import email1
import json
import locale
import sys


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  global tahun_terbesar
  max_revenue = {"omset": 0,"car_name_omset":'','total_sales':0,'car_total_sales':''}
  year = {}
  tahun_terbesar_sales = 0
  for item in data:
    id_car = str(item["id"])
    car_make = item["car"]['car_make']
    car_model = item["car"]['car_model']
    car_year = item["car"]['car_year']
    model_car = '{} {} ({})'.format(car_make, car_model, car_year)
    price_car = item["price"]
    total_sales_car = item["total_sales"]
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    car_name = item['car']
    item_total_sales = item["total_sales"]
    if item_revenue > max_revenue["omset"]:
        max_revenue["omset"] = item_revenue
        max_revenue["car_name_omset"] = car_name
    # TODO: also handle max sales
    if item_total_sales > max_revenue['total_sales']:
        max_revenue['total_sales'] = item_total_sales
        max_revenue['car_total_sales'] = car_name
    # TODO: also handle most popular car_year
    if item["car"]['car_year'] not in year:
        year[item["car"]['car_year']] =item_total_sales
    else:
        year[item["car"]['car_year']] += item_total_sales
  for tahun, jumlah_penjualan in year.items():
      if jumlah_penjualan > tahun_terbesar_sales:
          tahun_terbesar_sales = jumlah_penjualan
          tahun_terbesar = tahun
  summary = [
      'The {} generated the most revenue: ${}'.format(
          format_car(max_revenue["car_name_omset"]), max_revenue["omset"]),
      'The {} had the most sales: {}'.format(
          format_car(max_revenue['car_total_sales']), max_revenue['total_sales']),
      'The most popular year was {} with {} sales.'.format(tahun_terbesar,tahun_terbesar_sales),
  ]
  return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    cwd = os.getcwd()
    data = load_data("{}/car_sales.json".format(cwd))
    summary = process_data(data)
    subject_line = "Sales summary for last month"
    email_body = "{}\n{}\n{}".format(summary[0],summary[1],summary[2])
    pdf_body = "{}<br/>{}<br/>{}".format(summary[0],summary[1],summary[2])
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))

    # TODO: turn this into a PDF report
    report1.generate("tmp/cars.pdf", subject_line, pdf_body, cars_dict_to_table(data))
    # TODO: send the PDF report as an email attachment
    message = email1.generate(sender, receiver, subject_line, email_body, "/tmp/cars.pdf")
    email1.send(message)

if __name__ == "__main__":
  main(sys.argv)




