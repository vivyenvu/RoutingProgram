import csv

addressIndex = []

# Populate list with index and associated address
with open('Address.csv') as csvf:
    addressCSV = csv.reader(csvf)
    for entry in addressCSV:
        addressIndex.append(entry)


def getAddressIndex(address):
    for row in addressIndex:
        if address == row[2]:
            return row[0] #cast as int if having issues
