import csv


with open('Distance.csv') as csvf:
    distanceCSV = csv.reader(csvf)
    distanceCSV = list(distanceCSV)
    # The csv. reader method returns a reader object which iterates over lines in the given CSV file. The numbers. csv file contains numbers

def distance(a, b):
    distance = distanceCSV[a][b]
    if distance == '':
        distance = distanceCSV[b][a]

    return float(distance)