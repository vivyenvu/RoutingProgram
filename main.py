# Author: Vivyen Vu
# Student ID: 009777954
# Title: C950 Data Structures and Algorithms II Routing Project

import csv
import datetime

import Truck

with open('Address.csv') as csvf2:
    addressCSV = csv.reader(csvf2)

with open('Distance.csv') as csvf3:
    distanceCSV = csv.reader(csvf3)

# Green: Deadline and group packages
truck1 = Truck.Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 21, 4, 17], '8:00')

# Yellow: Must be on truck 2, all EOD
truck2 = Truck.Truck([3, 18, 36, 38, 5, 8, 27, 35, 7, 39, 11, 24, 23, 10], '10:20') #not sure when depart time should be

# Blue: Delayed packages or EOD, leave after 9:05
# 25 needs to be delivered by 10:30am
# 9 has wrong address listed until 10:20am  410 S State St.,
truck3 = Truck.Truck([6, 9, 25, 28, 32, 26, 2, 33, 19, 22], '9:05')