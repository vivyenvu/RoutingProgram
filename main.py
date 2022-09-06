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


while True:
    try:
        menuInput = input('Please enter a number option from the menu above. ')
        isValid = int(menuInput)
    except ValueError:
        print('Invalid input. Please enter a valid number. ')
        continue
    if isValid != 1 and isValid != 2 and isValid != 3:
        print('Invalid input. Please enter a valid number. ')
        continue

    elif isValid == 1:
        goEnRoute(truck1, package_hashmap)
        goEnRoute(truck3, package_hashmap)
        # After truck1's driver returns to the hub, he will take truck2 and deliver those packages
        goEnRoute(truck2, package_hashmap)

        for i in range(1, 41):
            package = package_hashmap.lookup(i)
            id = str(i)
            address = str(package.address)
            city = str(package.city)
            state = str(package.state)
            zipcode = str(package.zipcode)
            deadline = str(package.deadline)
            weight = str(package.weight)
            status = str(package.status)
            time = str(package.deliveredTime)
            print(id + ' | ' + address + ' | ' + city + ' | ' + state + ' | ' + zipcode + ' | ' + deadline + ' | ' + weight + ' | ' + status + ' at ' +time)

        print('Truck 1 mileage: ' + str(round(truck1.mileage, 1)))
        print('Truck 2 mileage: ' + str(round(truck2.mileage, 1)))
        print('Truck 3 mileage: ' + str(round(truck3.mileage, 1)))
        print('Total mileage: ' + str(round (truck1.mileage + truck2.mileage + truck3.mileage, 1)))
        break

    elif isValid == 2:
        print('choice 2')
        break

    elif isValid == 3:
        print('exiting')
        exit()
