from abc import ABCMeta

class Address:
    def __init__(self, addressLine1, addressLine2, city, postalCode):
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.postalCode = postalCode
    def __str__(self):
        out = "{} | {} | {} | {}".format(self.addressLine1, self.addressLine2, self.city, self.postalCode)
        return out

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

class Student(Person):
    def __init__(self, fName, mName, lName, dateOfBirth, address, email, 
        studentStatus, mainGuardian, secondaryGuardian, schoolCurrEnrolled,
        gradeLevel, subjectsForHelp, needsOneOnOne, availableDays, preferredSchools):
            super().__init__(fName, mName, lName, dateOfBirth, address, email)
            self.studentStatus = studentStatus
            self.mainGuardian = mainGuardian
            self.secondaryGuardian = secondaryGuardian
            self.schoolCurrEnrolled = schoolCurrEnrolled
            self.gradeLevel = gradeLevel
            self.subjectForHelp = subjectsForHelp
            self.needsOneOnOne = needsOneOnOne
            self.availableDays = availableDays
            self.preferredSchools = preferredSchools
    
    def __str__(self):
        output = "{} | {} | {} | {} | {} | {} | {} | {} | {}".format(
            self.firstName, self.middleName, self.lastName,
            self.dateOfBirth.strftime("%x"),
            self.address,
            self.studentStatus,
            self.mainGuardian,
            self.secondaryGuardian,
            self.schoolCurrEnrolled
        )
        
        return output

class Guardian(Person):
    def __init__(self, fName, mName, lName, dateOfBirth, address, email, 
        guardianType, cellphone, students = ""):
            super().__init__(fName, mName, lName, dateOfBirth, address, email)
            self.guardianType = guardianType
            self.cellphone = cellphone
            self.students = students
    def __str__(self):
        output = "{} | {} | {} | {} | {} | {} | {}".format(
            self.firstName, self.middleName, self.lastName,
            self.dateOfBirth,
            self.address,
            self.email,
            self.cellphone
        )
        
        return output
