from abc import ABCMeta

class Person(metaclass = ABCMeta):
    currPersonId = 1000000
    def __init__(self, fName, mName, lName, dateOfBirth, address, email):
        self.personId = self.currPersonId+1
        self.firstName = fName
        self.middleName = mName
        self.lastName = lName
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.email = email
