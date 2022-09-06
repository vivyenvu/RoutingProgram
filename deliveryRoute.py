import datetime

from distance import distanceBetween


# This method determines the truck's delivery route based on the nearest neighbor algorithm.
# When the next closest package is determined, the time and miles to that next address is added
# to the truck and the package
def goOnRoute(truck, hashmap):
    # Updates status of all package in truck to "On route"
    # Time complexity = O(n)
    packageNumbers = truck.myPackages  # List of package numbers
    for num in packageNumbers:
        package = hashmap.lookup(num)
        package.onRoute()

    # This is the nearest neighbor algorithm where every package associated with the id in packageNumbers
    # will be compared to find which address is the closest to the current address. Once the closest
    # package is found, the truck and package will be updated with the amount of time and mileage it took
    # to deliver to that next package. This is repeated until all packages are delivered
    # Time complexity = O(n^2)
    address1 = truck.currentAddress
    currentDistance = 25
    packagesRemaining = len(packageNumbers)
    while packagesRemaining > 0:
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
        truck.updateTime(currentDistance)
        truck.addMiles(currentDistance)
        truck.updateAddress(address2)
        nextPackage.deliveredAt(truck.currentTime)
        nextPackage.deliveredStatus()
        address1 = address2
        packagesRemaining -= 1
        currentDistance = 25
        # REMOVE THIS IS YOU FIND ANOTHER WAY TO ACCOUNT FOR THE CHANGE IN PACKAGE9'S ADDRESSXX
        # This if-statement is to account for package 9's change in address at 10:20am
        # Time complexity = O(1)
        if truck.currentTime >= datetime.timedelta(hours=10, minutes=20):
            package9 = hashmap.lookup(9)
            package9.address = '410 S State St'

    # Add miles and time from the truck's last address back to the hub
    truck.updateTime(distanceBetween(truck.currentAddress, '4001 South 700 East'))
    truck.addMiles(distanceBetween(truck.currentAddress, '4001 South 700 East'))
    truck.currentAddress = '4001 South 700 East'
