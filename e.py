# e) {'Jim': {' Gender': ' M', ' Age': ' 30', ' Salary': ' 5000'}, 'Joe': {...}...}

import csv

data_dict = {}
with open('to_dict.csv') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        key = row.pop('Name')
        data_dict[key] = row
print(data_dict)