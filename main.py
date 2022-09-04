import csv

with open('Package.csv') as csvf1:
    packageCSV = csv.reader(csvf1)

with open('Address.csv') as csvf2:
    addressCSV = csv.reader(csvf2)

with open('Distance.csv') as csvf3:
    distanceCSV = csv.reader(csvf3)
