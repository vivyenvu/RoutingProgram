import csv
from HashMap import HashMap
from Package import Package

# Create new hashmap to fill with package objects from Package.csv
package_hashmap = HashMap()
fileName = 'Package.csv'


# Get contents from CSV file O(N^2)
def csv_hashmap(fileName):
    with open(fileName) as csvf:
        contents = csv.reader(csvf)

        # Create a package object from each entry O(N)
        for entry in contents:
            id = entry[0]
            address = entry[1]
            city = entry[2]
            state = entry[3]
            zipcode = entry[4]
            deadline = entry[5]
            weight = entry[6]
            newPackage = Package(id, address, city, state, zipcode, deadline, weight, 'In hub')

            # Add package to hashmap
            package_hashmap.add(id, newPackage)
