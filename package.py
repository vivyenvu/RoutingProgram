# Creates class for package object
class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.deliveredTime = None

    def deliveredStatus(self):
        self.status = 'Delivered'

    def deliveredAt(self, time):
        self.deliveredTime = time

    def onRoute(self):
        self.status = 'On route'


