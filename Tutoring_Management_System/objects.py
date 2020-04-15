from abc import ABCMeta

class Person(metaclass = ABCMeta):
    currPersonId = 1000000
    def __init__(self, fName, lName, email):
        self.personId = self.currPersonId+1
        self.firstName = fName
        self.lastName = lName
        self.email = email

class Student(Person):
    def __init__(self, fName, lName, email, gradeLevel):
            super().__init__(fName, lName, email)
            self.gradeLevel = gradeLevel

    def __str__(self):
        output = "{} | {} | {} | {}".format(
            self.firstName, 
            self.lastName, 
            self.email, 
            self.gradeLevel
        )
        return output

class Guardian(Person):
    def __init__(self, fName, lName, email, guardianType, isMainContact):
            super().__init__(fName, lName, email)
            self.guardianType = guardianType
            self.isMainContact = isMainContact

    def __str__(self):
        output = "{} | {} | {} | {} | {}".format(
            self.firstName, self.lastName,
            self.email,
            self.guardianType,
            self.isMainContact
        )
        return output

class Tutors(Person):
    def __init__(self, fName, lName, email):
        super().__init__(fName, lName, email)

    def __str__(self):
        output = "{} | {} | {}".format(
            self.firstName, 
            self.lastName,
            self.email
        )
        return output

class Subjects():
    def __init__(self, subjectName):
        self.subjectName = subjectName

    def __str__(self):
        output = "{}".format(self.subjectName)
        return output

class Weekdays():
    def __init__(self, weekdayName):
        self.weekdayName = weekdayName
    
    def __str__(self):
        output = "{}".format(self.weekdayName)
        return output

class Schools():
    def __init__(self, schoolName, schoolPhone, schoolEmail):
        self.schoolName = schoolName
        self.schoolPhone = schoolPhone
        self.schoolEmail = schoolEmail

    def __str__(self):
        output = "{} | {} | {}".format(
            self.schoolName,
            self.schoolPhone,
            self.schoolEmail
        )
        return output