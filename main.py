# Author: Vivyen Vu
# Student ID: 009777954

# For the entire project:
# Time complexity = O(n^2)
# Space complexity = O(n)

import datetime
import truck
from deliveryRoute import goEnRoute
from hashMap import HashMap
from package_hashmap import csv_hashmap
from timeInfo import mileageAtTime, allPackagesAtTime, singlePackageAtTime

usableTime = None
# Green: Packages that have a specific deadline or must be grouped with other packages
truck1 = truck.Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 21, 4, 17], datetime.timedelta(hours=8))

# Yellow: Packages that must be on truck 2. All of their deadlines are EOD
truck2 = truck.Truck([3, 18, 36, 38, 5, 8, 27, 35, 7, 39, 11, 24, 23, 10, 9],
                     datetime.timedelta(hours=10))  # Depart after truck1's driver returns to the hub

# Blue: Delayed packages or have deadline of EOD. This truck must leave after 9:05
# 25 needs to be delivered by 10:30am
# 9 has wrong address listed until 10:20am  410 S State St.
truck3 = truck.Truck([6, 25, 28, 32, 26, 2, 33, 12, 22], datetime.timedelta(hours=9, minutes=5))

# Load packages from Package.csv into package_Hashmap
package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)


# Runs application in CLI
# Time complexity = O(n^2)
# Space complexity = O(1)
class Main:
    # Show user menu options
    # Time complexity = O(1)
    print('Welcome to the WGUPS Routing Program')
    print('What can I help you with today?')
    print('1 - Show status of all packages and trucks at the end of the day')
    print('2 - Show status of all packages and trucks at a given time')
    print('3 - Show status of a single packages at a given time')
    print('4 - Exit application')

    while True:
        try:
            menuInput = input('Please enter a number option from the menu above. ')
            isValid = int(menuInput)
        except ValueError:
            print('Invalid input. Please enter a valid number. ')
            continue
        if isValid != 1 and isValid != 2 and isValid != 3 and isValid != 4:
            print('Invalid input. Please enter a valid number. ')
            continue

        # Time complexity = O(n^2)
        # Space complexity = O(1)
        elif isValid == 1:
            # Trucks deliver all of their packages in this order
            goEnRoute(truck1, package_hashmap)
            goEnRoute(truck3, package_hashmap)
            # After truck1 returns to the hub at 9:57:40, driver will take truck2 and deliver those packages at 10:00
            goEnRoute(truck2, package_hashmap)

            # Print status of all packages after they've all been delivered
            print('STATUS OF ALL PACKAGES WHEN DAY ENDS')
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
                print(
                    id + ' | ' + address + ' | ' + city + ' | ' + state + ' | ' + zipcode + ' | ' + deadline + ' | ' + weight + ' | ' + status + ' at ' + time)

            # Print individual and total truck mileage
            print('Truck 1 mileage: ' + str(round(truck1.mileage, 1)))
            print('Truck 2 mileage: ' + str(round(truck2.mileage, 1)))
            print('Truck 3 mileage: ' + str(round(truck3.mileage, 1)))
            print('Total mileage: ' + str(round(truck1.mileage + truck2.mileage + truck3.mileage, 1)))

            # Print out which truck finished delivering packages last as time when all packages were delivered by
            endTime = datetime.timedelta(hours=17)
            if truck1.currentTime > truck2.currentTime and truck1.currentTime > truck3.currentTime:
                endTime = truck1.currentTime
            elif truck2.currentTime > truck1.currentTime and truck2.currentTime > truck3.currentTime:
                endTime = truck2.currentTime
            elif truck3.currentTime > truck1.currentTime and truck3.currentTime > truck1.currentTime:
                endTime = truck1.currentTime
            print('All packages were done being delivered by: ' + str(endTime))
            break

        # Time complexity = O(n^2)
        # Space complexity = O(1) DOUBLE CHECK THIS AFTER I ENTER OPTION TO SEARCH SINGLE PACKAGE DSFGI;LDFHGLKHAD;LGKHDFA;HG;
        elif isValid == 2:
            try:
                # Convert time entered by user in to timedelta so that it can be compared to truck and package timedelta
                timeInput = input(
                    'Please enter the time you would like to check all package status in hh:mm:ss format. ')
                timeParts = timeInput.split(':')
                usableTime = datetime.timedelta(hours=int(timeParts[0]), minutes=int(timeParts[1]),
                                                seconds=int(timeParts[2]))

                # Update package information at user given time
                print('STATUS OF ALL PACKAGES AT ' + str(usableTime))
                allPackagesAtTime(truck1, usableTime, package_hashmap)
                allPackagesAtTime(truck2, usableTime, package_hashmap)
                allPackagesAtTime(truck3, usableTime, package_hashmap)

                # Get truck mileage at user given time
                mile1 = mileageAtTime(truck1, usableTime, package_hashmap)
                mile2 = mileageAtTime(truck2, usableTime, package_hashmap)
                mile3 = mileageAtTime(truck3, usableTime, package_hashmap)

                # Print individual and total truck mileage
                print('Truck 1 mileage: ' + str(round(mile1, 1)))
                print('Truck 2 mileage: ' + str(round(mile2, 1)))
                print('Truck 3 mileage: ' + str(round(mile3, 1)))
                print('Total mileage: ' + str(round(mile1 + mile2 + mile3, 1)))
                exit()
            except ValueError:
                print('Invalid input. Restart program and try again. ')
                exit()
            except IndexError:
                print('Invalid input. Restart program and try again. ')
                exit()

        elif isValid == 3:
            try:
                # Convert time entered by user in to timedelta so that it can be compared to truck and package timedelta
                timeInput = input(
                    'Please enter the time you would like to check the status of this package in hh:mm:ss format. ')
                timeParts = timeInput.split(':')
                usableTime = datetime.timedelta(hours=int(timeParts[0]), minutes=int(timeParts[1]),
                                                seconds=int(timeParts[2]))

                packageId = int(input('Please enter the id of the package you would like to check '))
                if packageId < 1 or packageId > 40:
                    print('Invalid package id. Restart program and try again. ')
                    exit()

                goEnRoute(truck1, package_hashmap)
                goEnRoute(truck3, package_hashmap)
                # After truck1 returns to the hub at 9:57:40, driver will take deliver truck2's packages at 10
                goEnRoute(truck2, package_hashmap)

                # Update package information at user given time
                print('STATUS OF PACKAGE #'+str(packageId)+' AT ' + str(usableTime))
                singlePackageAtTime(packageId, usableTime, package_hashmap)

                exit()
            except ValueError:
                print('Invalid input. Restart program and try again. ')
                exit()
            except IndexError:
                print('Invalid input. Restart program and try again. ')
                exit()

        # Time complexity = O(1)
        # Space complexity = O(1)
        elif isValid == 4:
            print('You are exiting the application. ')
            exit()
