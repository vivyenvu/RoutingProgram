# Creates class for Truck object
import datetime


class Truck:
    # Constructor for Truck where maxPackages, speed, mileage, and currentAddress are preset according to
    # project details
    def __init__(self, myPackages, departTime):
        self.maxPackages = 16
        self.speed = 18
        self.myPackages = myPackages
        self.mileage = 0.0
        self.currentAddress = '4001 South 700 East'
        self.departTime = departTime
        self.currentTime = departTime

    # Sets truck's current address to a new address
    def updateAddress(self, newAddress):
        self.currentAddress = newAddress

    # Calculates time elapsed to travel a certain amount of miles, and adds that to the truck's currentTime
    def updateTime(self, miles):
        elapsedTime = datetime.timedelta(seconds=((miles / 18) * 60 * 60))
        self.currentTime = self.currentTime + elapsedTime

    # Adds input miles to truck's total mileage
    def addMiles(self, miles):
        self.mileage += miles
