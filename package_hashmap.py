import csv
from package import Package


# Get contents from CSV file, create packages from each row, and put it in the hashName HashMap O(N^2)
def csv_hashmap(fileName, hashName):
    tempList = []
    with open(fileName, encoding='utf-8-sig') as csvf:
        contents = csv.reader(csvf)
        for entry in contents:
            tempList.append(entry)

        # Create a package object from each entry O(N)
        for item in tempList:
            id = int(item[0])
            address = item[1]
            city = item[2]
            state = item[3]
            zipcode = item[4]
            deadline = item[5]
            weight = item[6]
            newPackage = Package(id, address, city, state, zipcode, deadline, weight)

            # Add package to hashmap
            hashName.insert(id, newPackage)
