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
        for i in range(len(packageNumbers)):
            addressTemp = package_hashmap.lookup(packageNumbers[i]).address
            if distanceBetween(address1, addressTemp) < distanceBetween(address1, closestAddress):
                address2 = addressTemp
                nextPackage = package_hashmap.lookup(packageNumbers[i])
                removeValue = i

        packagesRemaining -= 1
        packageNumbers.remove(removeValue)
        truck.updateTime(distanceBetween(address1, address2))
        truck.addMiles(distanceBetween(address1, address2))
        truck.updateAddress(address2)
        package_hashmap.lookup(packageNumbers[removeValue]).deliveredAt(truck.currentTime)
        package_hashmap.lookup(packageNumbers[removeValue]).deliveredStatus()



    #truck.setRoute(orderedRoute) # my not be necessary
