import datetime

from deliveryRoute import goEnRoute


def packageAtTime(truck, usableTime, package_hashmap):
    packageNumbers = []
    for nums in truck.myPackages:
        packageNumbers.append(nums)
    depart = truck.departTime
    goEnRoute(truck, package_hashmap)

    for num in packageNumbers:
        package = package_hashmap.lookup(num)
        if package.deliveredTime < usableTime:
            pass
        elif depart < usableTime:
            package.enRoute()
            package.deliveredTime = None
        elif usableTime <= depart:
            package.inHub()
            package.deliveredTime = None
        id = str(num)
        address = str(package.address)
        city = str(package.city)
        state = str(package.state)
        zipcode = str(package.zipcode)
        deadline = str(package.deadline)
        weight = str(package.weight)
        status = str(package.status)
        time = str(package.deliveredTime)
        if package.deliveredTime is None:
            print(
                id + ' | ' + address + ' | ' + city + ' | ' + state + ' | ' + zipcode + ' | ' + deadline + ' | ' + weight + ' | ' + status)
        else:
            print(
                id + ' | ' + address + ' | ' + city + ' | ' + state + ' | ' + zipcode + ' | ' + deadline + ' | ' + weight + ' | ' + status + ' at ' + time)


def mileageAtTime(truck, usableTime, package_hashmap):
    goEnRoute(truck, package_hashmap)
    timedMiles = 0.0
    if truck.currentTime < usableTime:
        timedMiles = truck.mileage
    elif usableTime < truck.departTime:
        timedMiles = 0.0
    elif truck.departTime < usableTime:
        timeDif = usableTime - truck.departTime
        timeDifInMins = timeDif / datetime.timedelta(minutes=1)
        timedMiles = timeDifInMins * 0.3

    return timedMiles
