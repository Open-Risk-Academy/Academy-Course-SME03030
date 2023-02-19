# (c) 2021 - 2023 Open Risk (https://www.openriskmanagement.com)

import csv

filehandle = open("portfolio.csv", "r")
reader = csv.reader(filehandle, delimiter=',')
for row in reader:
    print(row[1])
