import csv

from address import getAddressIndex

distancesBtwn = []
distanceDict = {}
filename = 'Distance.csv'

# Populate list with distances in between two addresses
with open(filename, encoding='utf-8-sig') as csvf:
    distanceCSV = csv.reader(csvf)
    for entry in distanceCSV:
        distancesBtwn.append(entry)

# Create a dictionary with key: address index, and value: distances between that index and other address indexes
for x in range(0, len(distancesBtwn)):
    distanceDict[x] = distancesBtwn[x]


def distanceBetween(address1, address2):
    a1 = getAddressIndex(address1)
    a2 = getAddressIndex(address2)
    distance = distanceDict[a1][a2]
    if distance == '':
        distance = distanceDict[a2][a1]

    return float(distance)
