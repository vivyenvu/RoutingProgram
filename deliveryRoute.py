import datetime

from distance import distanceBetween


# This method determines the truck's delivery route based on the nearest neighbor algorithm.
# When the next closest package is determined, the time and miles to that next address is added
# to the truck and the package
# Time complexity = O(n^2)
# Space complexity = O(1)
def goEnRoute(truck, hashmap):
    # Make copy of the list of package numbers on this truck
    packageNumbers = truck.myPackages

    # Iterate through list of package numbers
    # Time complexity = O(n)
    for num in packageNumbers:
        # Look up the package using its id in the hashmap of packages
        package = hashmap.lookup(num)
        # Update status of all package in truck to "En route"
        package.enRoute()

    # Set currentDistance to a number that exceeds any possible distance between any two packages based on Address.csv
    currentDistance = 25
    # Get the number of packages remaining in the truck that need to be delivered by
    # getting the length of the packageNumbers list.
    packagesRemaining = len(packageNumbers)
    # Iterate through the remaining packages
    while packagesRemaining > 0:
        # Keep track of package to remove
        removeId = packageNumbers[0]

        # If the truck's current time is after 10:20, update package9's address and zipcode
        if truck.currentTime >= datetime.timedelta(hours=10, minutes=20):
            package9 = hashmap.lookup(9)
            package9.address = '410 S State St'
            package9.zipcode = '84111'

        # Iterate through all the packages remaining in the truck to find the nearest package address
        for num in packageNumbers:
            # Get address of package
            packageAddress = hashmap.lookup(num).address
            # Get distance between truckAddress and packageAddress
            packageDistance = distanceBetween(truck.currentAddress, packageAddress)
            # Check if packageDistance is shortest so far
            if packageDistance < currentDistance:
                # If so, assume this package is next to be delivered
                nextAddress = packageAddress
                nextPackage = hashmap.lookup(num)
                currentDistance = distanceBetween(truck.currentAddress, nextAddress)
                removeId = num

        # Remove package with the nearest address from list of packages
        packageNumbers.remove(removeId)
        # Add time it took to deliver the nearest package to truck's currentTime
        truck.updateTime(currentDistance)
        # Add miles it took to deliver the nearest package to the truck's mileage
        truck.addMiles(currentDistance)
        # Set truck's current address to address of package that was just delivered
        truck.updateAddress(nextAddress)
        # Set package's deliveredTime to be the truck's currentTime
        nextPackage.deliveredAt(truck.currentTime)
        # Set package's status to 'Delivered'
        nextPackage.deliveredStatus()
        # Subtract 1 from the number of packages remaining
        packagesRemaining -= 1
        # Reset currentDistant to exceed any possible distance between any two packages based on Address.csv
        currentDistance = 25

    # Calculate miles and time from truck's last address back to the hub. Add that to truck's information
    truck.updateTime(distanceBetween(truck.currentAddress, '4001 South 700 East'))
    truck.addMiles(distanceBetween(truck.currentAddress, '4001 South 700 East'))
    truck.currentAddress = '4001 South 700 East'
