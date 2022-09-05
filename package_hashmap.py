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
        for row in contents:
            id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            newPackage = Package(id, address, city, state, zipcode, deadline, weight, 'In hub')

            # Add package to hashmap
            package_hashmap.insert(id, newPackage)
