from abc import ABCMeta

class Person(metaclass = ABCMeta):
    currPersonId = 1000
    def __init__(self, fName, lName, email):
        self.personId = self.currPersonId+1
        self.firstName = fName
        self.lastName = lName
        self.email = email

class Student(Person):
    def __init__(
        self, fName, lName, email, mainGuardian, 
        gradeLevel, subjectsForHelp, availableDays, preferredSchools
    ):
            super().__init__(fName, lName, email)
            self.gradeLevel = gradeLevel
            self.mainGuardian = mainGuardian
            self.subjectsForHelp = subjectsForHelp
            self.availableDays = availableDays
            self.preferredSchools = preferredSchools

    def __str__(self):
        output = "{} | {} | {} | {} | {}".format(
            self.personId,
            self.firstName, 
            self.lastName, 
            self.email, 
            self.gradeLevel
        )
        return output

class Guardian(Person):
    def __init__(self, fName, lName, email, guardianType, isMainContact, students_list):
            super().__init__(fName, lName, email)
            self.guardianType = guardianType
            self.isMainContact = isMainContact
            self.students_list = students_list

    def __str__(self):
        output = "{} | {} | {} | {} | {}".format(
            self.firstName, self.lastName,
            self.email,
            self.guardianType,
            self.isMainContact
        )
        return output

class Tutor(Person):
    def __init__(self, fName, lName, email):
        super().__init__(fName, lName, email)

    def __str__(self):
        output = "{} | {} | {}".format(
            self.firstName, 
            self.lastName,
            self.email
        )
        return output

class Subject():
    def __init__(self, subjectName):
        self.subjectName = subjectName

    def __str__(self):
        output = "{}".format(self.subjectName)
        return output

class Weekday():
    def __init__(self, weekdayName):
        self.weekdayName = weekdayName
    
    def __str__(self):
        output = "{}".format(self.weekdayName)
        return output

class School():
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