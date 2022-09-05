# Nearest neighbor algorithm
from distance import distanceBetween
from hashMap import HashMap
from package_hashmap import csv_hashmap
from address import getAddressIndex

# delete these later
package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)


def goOnRoute(truck):
    global removeIndex
    orderedRoute = [] # may not be necessary
    packageNumbers = truck.myPackages # List of package numbers
    packagesRemaining = len(packageNumbers)

    address1 = truck.currentAddress
    closestAddress = package_hashmap.lookup(packageNumbers[0]).address
    print(closestAddress) #test

    print('DELIVERY ROUTE')
    print(packageNumbers)
    while packagesRemaining > 0:
        for i in range(len(packageNumbers)):
            addressTemp = package_hashmap.lookup(packageNumbers[i]).address
            if distanceBetween(address1, addressTemp) < distanceBetween(address1, closestAddress):
                address2 = addressTemp
                nextPackage = package_hashmap.lookup(packageNumbers[i])
                removeThis= packageNumbers[i]
                removeIndex = i

        #packageNumbers.remove(removeThis)
        print(removeIndex)
        del packageNumbers[removeIndex]
        print(packageNumbers)
        truck.updateTime(distanceBetween(address1, address2))
        truck.addMiles(distanceBetween(address1, address2))
        truck.updateAddress(address2)
        nextPackage.deliveredAt(truck.currentTime)
        nextPackage.deliveredStatus()
        address1 = address2
        packagesRemaining -= 1



    #truck.setRoute(orderedRoute) # my not be necessary
