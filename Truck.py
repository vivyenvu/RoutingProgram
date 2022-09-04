# Creates class for Truck object
import datetime


class Truck:
    def __init__(self, myPackages, mileage, currentAddress, departTime):
        self.maxPackages = 16
        self.speed = 18
        self.myPackages = myPackages
        self.mileage = mileage
        self.currentAddress = currentAddress
        self.departTime = departTime
        self.currentTime = datetime.timedelta()

