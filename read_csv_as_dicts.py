# Write a function to read a CSV file and return data as a list of dictionaries
""" import csv
file_path = "test.csv"
data_list = []
with open(file_path, mode='r', newline='') as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        data_list.append(dict(row))
    print(data_list[:3]) """

import csv
def read_csv_as_dicts(file_path):
    data_list=[]
    with open(file_path, mode='r', newline='') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            data_list.append(dict(row))
        print(data_list[:3])

file_path="test.csv"
read_csv_as_dicts(file_path)