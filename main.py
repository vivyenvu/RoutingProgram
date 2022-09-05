# Author: Vivyen Vu
# Student ID: 009777954
# Title: C950 Data Structures and Algorithms II Routing Project

import csv
import datetime

import truck
from address import addressIndex, getAddressIndex
from distance import distanceCSV, distanceDict, distanceBetween
from hashMap import HashMap
from package_hashmap import csv_hashmap

# Green: Deadline and group packages
truck1 = truck.Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 21, 4, 17], datetime.timedelta(hours=8))

# Yellow: Must be on truck 2, all EOD
truck2 = truck.Truck([3, 18, 36, 38, 5, 8, 27, 35, 7, 39, 11, 24, 23, 10], datetime.timedelta(hours=11))  # not sure when depart time should be

# Blue: Delayed packages or EOD, leave after 9:05
# 25 needs to be delivered by 10:30am
# 9 has wrong address listed until 10:20am  410 S State St.,
truck3 = truck.Truck([6, 9, 25, 28, 32, 26, 2, 33, 19, 22], datetime.timedelta(hours=9, minutes=5))


class Main:
    package_hashmap = HashMap()
    csv_hashmap('Package.csv', package_hashmap)

    print('Welcome to the start of the program \n')
    print(package_hashmap)
    print('Address[]')
    print(addressIndex)
    print('This is the dict')
    print(distanceDict)

    print(distanceBetween('3148 S 1100 W', '2010 W 500 S'))
    print(truck3.departTime)
    truck3.updateTime(4.1)
    print(truck3.currentTime)