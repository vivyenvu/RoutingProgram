# Nearest neighbor algorithm
from distance import distanceBetween


def goOnRoute(truck, hashmap):
    # UPDATE ALL PACKAGE STATUS TO ON ROUTE
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

        # DO I NEED TO ADD DISTANCE FROM LAST ADDRESS BACK TO HUB TO THE TRUCK'S MILEAGE
