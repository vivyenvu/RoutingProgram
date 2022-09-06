# Nearest neighbor algorithm
from distance import distanceBetween


def goOnRoute(truck, hashmap):
    # Updates all package status in truck to "On route"
    packageNumbers = truck.myPackages  # List of package numbers
    for num in packageNumbers:
        package = hashmap.lookup(num)
        package.onRoute()
    packagesRemaining = len(packageNumbers)
    # print('DELIVERY ROUTE')
    address1 = truck.currentAddress
    currentDistance = 25
    while packagesRemaining > 0:
        # print(packageNumbers)
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
        # print('Current distance: '+ str(currentDistance))
        # print('Current mileage: '+str(truck.mileage))
        truck.updateAddress(address2)
        nextPackage.deliveredAt(truck.currentTime)
        nextPackage.deliveredStatus()
        address1 = address2
        packagesRemaining -= 1
        currentDistance = 25
        # print("TRUCK'S CURRENT TIME")
        # print(truck.currentTime)
        # print(truck.mileage)

    # Add miles and time from the truck's last address back to the hub
    truck.updateTime(distanceBetween(truck.currentAddress, '4001 South 700 East'))
    truck.addMiles(distanceBetween(truck.currentAddress, '4001 South 700 East'))
    truck.currentAddress = '4001 South 700 East'

