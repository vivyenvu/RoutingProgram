import csv

# Empty list to hold index value associated with each address from Address.csv
addressIndex = []

# Overall:
# Time complexity = O(n)
# Space complexity = O(n)

# Populate list with index and associated address from Address.csv
# Time complexity = O(n)
# Space complexity = O(n)
with open('Address.csv', encoding='utf-8-sig') as csvf:
    addressCSV = csv.reader(csvf)
    for entry in addressCSV:
        addressIndex.append(entry)


# Returns the index associated with a given address
# Time complexity = O(n)
def getAddressIndex(address):
    for row in addressIndex:
        if address == row[2]:
            return int(row[0])
