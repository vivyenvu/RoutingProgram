import csv


with open('Distance.csv') as csvf:
    distanceCSV = csv.reader(csvf)
    distanceCSV = list(distanceCSV)

def distance(a, b):
    distance = distanceCSV[a][b]
    if distance == '':
        distance = distanceCSV[b][a]

    return float(distance)