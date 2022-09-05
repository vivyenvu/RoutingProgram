import csv

addressIndex = []

# Populate list with index and associated address
with open('Address.csv', encoding='utf-8-sig') as csvf:
    addressCSV = csv.reader(csvf)
    for entry in addressCSV:
        addressIndex.append(entry)


def getAddressIndex(address):
    for row in addressIndex:
        if address == row[2]:
            return int(row[0])
