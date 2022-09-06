# Author: Vivyen Vu
# Student ID: 009777954
# Title: C950 Data Structures and Algorithms II Routing Project


import datetime

import truck
from address import addressIndex
from deliveryRoute import goOnRoute
from distance import distanceDict, distanceBetween
from hashMap import HashMap
from package_hashmap import csv_hashmap

# Green: Deadline and group packages
truck1 = truck.Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 21, 4, 17], datetime.timedelta(hours=8))

# Yellow: Must be on truck 2, all EOD
truck2 = truck.Truck([3, 18, 36, 38, 5, 8, 27, 35, 7, 39, 11, 24, 23, 10],
                     datetime.timedelta(hours=10))  # Depart after truck1's driver returns to the hub

# Blue: Delayed packages or EOD, leave after 9:05
# 25 needs to be delivered by 10:30am
# 9 has wrong address listed until 10:20am  410 S State St. CHECK ON THIS AS;LKDA;OIESGA;LESR;ALKSDHGLKASDJG;LKASDF;SLDKJ;ALSDHGO;AIREG;LSHG;ALSIGH
truck3 = truck.Truck([6, 9, 25, 28, 32, 26, 2, 33, 12, 22], datetime.timedelta(hours=9, minutes=5))



class Main:
    package_hashmap = HashMap()
    csv_hashmap('Package.csv', package_hashmap)
    # if truck3.currentTime > datetime.timedelta(hours=10, minutes=20):
    #    package9 = package_hashmap.lookup(9)
    #    package9.address = '410 S State St'

    goOnRoute(truck1, package_hashmap)
    goOnRoute(truck3, package_hashmap)
    # After truck1's driver returns to the hub, he will take truck2 and deliver those packages
    goOnRoute(truck2, package_hashmap)
    print(truck1.currentTime)
    print(truck2.currentTime)
    print(truck3.currentTime)
    print('TOTAL MILEAGE')
    print(truck1.mileage + truck2.mileage + truck3.mileage)
    thing = package_hashmap.lookup(5)

    #print(package_hashmap.lookup(5))
    for i in range(1, 41):
        package = package_hashmap.lookup(i)
        id = str(i)
        time = str(package.deliveredTime)
        print('Package number '+id+ ' was delivered at '+time)

    # print('Welcome to the start of the program \n')

    # print('Address[]')
    # print(addressIndex)
    # print('This is the dict')
    # print(distanceDict)

    # print(distanceBetween('3148 S 1100 W', '2010 W 500 S'))
    # print(truck3.departTime)
    # truck3.updateTime(4.1)
    # print(truck3.currentTime)
