# Nearest neighbor algorithm
from distance import distanceBetween
from hashMap import HashMap
from package_hashmap import csv_hashmap
from address import getAddressIndex

# delete these later
package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)


def goOnRoute(truck):
    orderedRoute = [] # may not be necessary
    packageNumbers = truck.myPackages # List of package numbers
    packagesRemaining = len(packageNumbers)

    address1 = truck.currentAddress
    closestAddress = package_hashmap.lookup(packageNumbers[0]).address
    print(closestAddress)
    while packagesRemaining > 0:
        for i in packageNumbers:

            addressTemp = package_hashmap.lookup(packageNumbers)[1]
            if distanceBetween(address1, addressTemp) < distanceBetween(address1, shortestDistance):
                shortestDistance = addressTemp
                removeValue = i

        packageNumbers.remove(removeValue)
        packagesRemaining -= 1

        truck.setRoute(orderedRoute) # my not be necessary
