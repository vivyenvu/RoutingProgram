# Nearest neighbor algorithm
from hashMap import HashMap
from package_hashmap import csv_hashmap

# delete these later
package_hashmap = HashMap()
csv_hashmap('Package.csv', package_hashmap)
def deliverRoute(truck):
    orderedRoute = []
    packageList = truck.myPackages
    address1 = truck.currentAddress
    for i in packageList:
        addressTemp = packageList.lookUp(i)

    truck.setRoute(orderedRoute)


