# Author: Vivyen Vu
# Student ID: 009777954


import datetime
import truck
from address import addressIndex
from deliveryRoute import goEnRoute
from hashMap import HashMap
from package_hashmap import csv_hashmap

# Green: Packages that have a specific deadline or must be grouped with other packages
truck1 = truck.Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 21, 4, 17], datetime.timedelta(hours=8))

# Yellow: Packages that must be on truck 2. All of their deadlines are EOD
truck2 = truck.Truck([3, 18, 36, 38, 5, 8, 27, 35, 7, 39, 11, 24, 23, 10],
                     datetime.timedelta(hours=10))  # Depart after truck1's driver returns to the hub

# Blue: Delayed packages or have deadline of EOD. This truck must leave after 9:05
# 25 needs to be delivered by 10:30am
# 9 has wrong address listed until 10:20am  410 S State St.
truck3 = truck.Truck([6, 9, 25, 28, 32, 26, 2, 33, 12, 22], datetime.timedelta(hours=9, minutes=5))

package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)


# if truck3.currentTime > datetime.timedelta(hours=10, minutes=20):
#    package9 = package_hashmap.lookup(9)
#    package9.address = '410 S State St'
class Main:
    print('Welcome to the WGUPS Routing Program')
    print('What can I help you with today?')
    print('1 - Show status of all packages at the end of the day')
    print('2 - Show status of all packages at a given time')
    print('3 - Exit application')
    menuInput = input('Please enter a number option from the menu above. ')

    try:
        isValid = int(menuInput)
    except ValueError:
        menuInput = input('Invalid input. Please enter a valid number. ')

    if isValid !=1 and isValid !=2 and isValid !=3:
        menuInput = input('Invalid input. Please enter a valid number. ')
    else:

        goEnRoute(truck1, package_hashmap)
        goEnRoute(truck3, package_hashmap)
        # After truck1's driver returns to the hub, he will take truck2 and deliver those packages
        goEnRoute(truck2, package_hashmap)

        print('Truck 1 mileage: ' + str(truck1.mileage))
        print('Truck 2 mileage: ' + str(truck2.mileage))
        print('Truck 3 mileage: ' + str(truck3.mileage))
        print('Total mileage: '+str(truck1.mileage + truck2.mileage + truck3.mileage))

        # print(package_hashmap.lookup(5))
        for i in range(1, 41):
            package = package_hashmap.lookup(i)
            id = str(i)
            time = str(package.deliveredTime)
            print('Package number ' + id + ' was delivered at ' + time)

        # print('Welcome to the start of the program \n')

        # print('Address[]')
        # print(addressIndex)
        # print('This is the dict')
        # print(distanceDict)

        # print(distanceBetween('3148 S 1100 W', '2010 W 500 S'))
        # print(truck3.departTime)
        # truck3.updateTime(4.1)
        # print(truck3.currentTime)
