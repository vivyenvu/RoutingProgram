# Nearest neighbor algorithm
from distance import distanceBetween
from hashMap import HashMap
# from package_hashmap import csv_hashmap

# delete these later
# package_hashmap = HashMap()
# csv_hashmap('Package.csv', package_hashmap)


def goOnRoute(truck, hashmap):
    packageNumbers = truck.myPackages  # List of package numbers
    packagesRemaining = len(packageNumbers)
    print('DELIVERY ROUTE')
    address1 = truck.currentAddress
    currentDistance = 25
    while packagesRemaining > 0:
        print(packageNumbers)
        removeThis = packageNumbers[0]
        for num in packageNumbers:
            addressTemp = hashmap.lookup(num).address
            tempDistance = distanceBetween(address1, addressTemp)
            if tempDistance < currentDistance:
                address2 = addressTemp
                nextPackage = hashmap.lookup(num)
                currentDistance = distanceBetween(address1, address2)
                removeThis = num

        packageNumbers.remove(removeThis)
        truck.updateTime(distanceBetween(address1, address2))
        truck.addMiles(distanceBetween(address1, address2))
        truck.updateAddress(address2)
        nextPackage.deliveredAt(truck.currentTime)
        nextPackage.deliveredStatus()
        address1 = address2
        packagesRemaining -= 1

        # DO I NEED TO ADD DISTANCE FROM LAST ADDRESS BACK TO HUB TO THE TRUCK'S MILEAGE
