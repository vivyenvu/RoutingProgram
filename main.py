# Author: Vivyen Vu
# Student ID: 009777954
# Title: C950 Data Structures and Algorithms II Routing Project

import csv

from HashMap import HashMap

with open('Package.csv') as csvf1:
    packageCSV = csv.reader(csvf1)

with open('Address.csv') as csvf2:
    addressCSV = csv.reader(csvf2)

with open('Distance.csv') as csvf3:
    distanceCSV = csv.reader(csvf3)

def open_csv(fileName, hashmap):

    package_hashmap = HashMap()