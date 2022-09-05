# Nearest neighbor algorithm
from distance import distanceBetween
from hashMap import HashMap
from package_hashmap import csv_hashmap
from address import getAddressIndex

# delete these later
package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)


def deliverRoute(truck):
    orderedRoute = [] # may not be necessary
    packageNumbers = truck.myPackages # List of package numbers
    address1 = truck.currentAddress
    shortestDistance = package_hashmap.lookup(packageNumbers[0])[1]

    for i in packageNumbers:
        addressTemp = package_hashmap.lookup(packageNumbers)[1]
        if distanceBetween(address1, addressTemp) < distanceBetween(address1, shortestDistance):
            shortestDistance = addressTemp

    truck.setRoute(orderedRoute) # my not be necessary
