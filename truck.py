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
        self.currentTime = departTime
        self.route = []

    def updateAddress(self, newAddress):
        self.currentAddress = newAddress

    def updateTime(self, miles):
        elapsedTime = datetime.timedelta(seconds=((miles / 18) * 60 * 60))
        self.currentTime = self.currentTime + elapsedTime

    def addMiles(self, miles):
        self.mileage = self.mileage + miles

    def setRoute(self, orderedRoute):
        self.route = orderedRoute

