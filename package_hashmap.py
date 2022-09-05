import csv
from package import Package


# Get contents from CSV file, create packages from each row, and put it in the hashName HashMap O(N^2)
def csv_hashmap(fileName, hashName):
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
            hashName.insert(id, newPackage)
