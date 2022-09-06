# Nearest neighbor algorithm
from distance import distanceBetween
from hashMap import HashMap
from package_hashmap import csv_hashmap
from address import getAddressIndex

# delete these later
package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)


def goOnRoute(truck):
    # orderedRoute = []  # may not be necessary
    packageNumbers = truck.myPackages  # List of package numbers
    packagesRemaining = len(packageNumbers)

    # address2 = package_hashmap.lookup(packageNumbers[0]).address
    # print(address2)  # test
    print('DELIVERY ROUTE')
    print(packageNumbers)

    address1 = truck.currentAddress
    currentDistance = 25
    while packagesRemaining > 0:
        removeThis = packageNumbers[0]
        for num in packageNumbers:
            addressTemp = package_hashmap.lookup(num).address
            tempDistance = distanceBetween(address1, addressTemp)
            if tempDistance < currentDistance:
                address2 = addressTemp
                nextPackage = package_hashmap.lookup(num)
                currentDistance = distanceBetween(address1, address2)
                removeThis = num

        packageNumbers.remove(removeThis)
        print(packageNumbers)
        # removeThis =
        truck.updateTime(distanceBetween(address1, address2))
        truck.addMiles(distanceBetween(address1, address2))
        truck.updateAddress(address2)
        nextPackage.deliveredAt(truck.currentTime)
        nextPackage.deliveredStatus()
        address1 = address2
        packagesRemaining -= 1

    # truck.setRoute(orderedRoute) # my not be necessary
