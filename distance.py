import csv

distancesBtwn = []
distanceDict = {}
filename = 'Distance.csv'

# Populate list with distances in between two addresses
with open(filename, newline='') as csvf:
    distanceCSV = csv.reader(csvf)
    for row in distanceCSV:
        distancesBtwn.append(row)

for x in range(0, len(distancesBtwn)):
    distanceDict[x] = distancesBtwn[x]



def distanceBetween(address1, address2):
    distance = distanceCSV[address1][address2]
    if distance == '':
        distance = distanceCSV[address2][address1]

    return float(distance)
