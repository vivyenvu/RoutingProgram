# Creates class for Truck object
import datetime


class Truck:
    def __init__(self, myPackages, departTime):
        self.maxPackages = 16
        self.speed = 18
        self.myPackages = myPackages
        self.mileage = 0.0
        self.currentAddress = '4001 South 700 East'
        self.departTime = departTime
        self.currentTime = datetime.timedelta()

