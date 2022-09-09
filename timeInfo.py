import datetime

from deliveryRoute import goEnRoute


# This method prints out package information at a user given time
# Time complexity = O(n)
# Space complexity = O(1)
def packageAtTime(truck, usableTime, package_hashmap):
    # Fill list packageNumbers with the id of packages in this truck
    packageNumbers = []
    for nums in truck.myPackages:
        packageNumbers.append(nums)
    depart = truck.departTime

    # Deliver all packages in this truck
    # Time complexity = O(n^2)
    # Space complexity = O(1)
    goEnRoute(truck, package_hashmap)

    # Update information of all packages according to the user given time
    # Time complexity = O(n)
    for num in packageNumbers:
        # Compare user given time to when package was delivered at end of the day
        package = package_hashmap.lookup(num)

        # If user asks for time after delivery, leave package information the same
        if package.deliveredTime < usableTime:
            pass

        # Otherwise, if user given time is after package leaving the hub, that package status will be set to 'En route'
        # and its deliveredTime will rest to None
        elif depart < usableTime:
            package.enRoute()
            package.deliveredTime = None

        # Otherwise, if user asks for time before truck left hub, all packages in truck will have status = 'In hub'
        # and their deliveredTime will reset to None
        elif usableTime <= depart:
            package.inHub()
            package.deliveredTime = None

        # Get individual package information to be printed in the status report
        id = str(num)
        address = str(package.address)
        city = str(package.city)
        state = str(package.state)
        zipcode = str(package.zipcode)
        deadline = str(package.deadline)
        weight = str(package.weight)
        status = str(package.status)
        time = str(package.deliveredTime)

        # If the package is en route or in hub, their status will be printed alone
        if package.deliveredTime is None:
            print(
                id + ' | ' + address + ' | ' + city + ' | ' + state + ' | ' + zipcode + ' | ' + deadline + ' | ' + weight + ' | ' + status)

        # Otherwise, if package has been delivered, status will be printed with deliveredTime
        else:
            print(
                id + ' | ' + address + ' | ' + city + ' | ' + state + ' | ' + zipcode + ' | ' + deadline + ' | ' + weight + ' | ' + status + ' at ' + time)


# This method returns truck mileage at a user given time
# Time complexity = O(n)
# Space complexity = O(n)
def mileageAtTime(truck, usableTime, package_hashmap):
    # The truck will deliver all packages
    # Time complexity = O(n)
    # Space complexity = O(n)
    goEnRoute(truck, package_hashmap)
    timedMiles = 0.0

    # If user asks for time after truck has finished delivering all packages, give the total amount of miles used
    # to deliver all packages
    # Time complexity = O(1)
    # Space complexity = O(1)
    if truck.currentTime < usableTime:
        timedMiles = truck.mileage

    # Otherwise, if user asks for a time before truck started delivering, give 0.0 miles
    elif usableTime < truck.departTime:
        timedMiles = 0.0

    # Otherwise, if user asks for a time when truck is en route, mileage is calculated based off how many minutes
    # since it has left the hub. 18 mph is equivalent to 0.3 miles per minute
    elif truck.departTime < usableTime:
        timeDif = usableTime - truck.departTime
        timeDifInMins = timeDif / datetime.timedelta(minutes=1)
        timedMiles = timeDifInMins * 0.3

    return timedMiles
