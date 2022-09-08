# Creates class for package object
class Package:
    # Constructor where deliveredTime is None, but all other fields are inputted when this is called
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = 'In hub'
        self.deliveredTime = None

    # Updates package's status to 'Delivered'
    # Time complexity = O(1)
    def deliveredStatus(self):
        self.status = 'Delivered'

    # Updates package's deliveredTime to the input time
    # Time complexity = O(1)
    def deliveredAt(self, time):
        self.deliveredTime = time

    # Updates package's status to 'En route'
    # Time complexity = O(1)
    def enRoute(self):
        self.status = 'En route'

    def inHub(self):
        self.status = 'In hub'


