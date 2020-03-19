from class_person import Person

class Student(Person):
    def __init__(self, fName, mName, lName, dateOfBirth, address, email, 
        studentStatus, mainGuardian, secondaryGuardian, schoolCurrEnrolled,
        gradeLevel, subjectsForHelp, needsOneOnOne, hasDisability, 
        disabilityDetails, availableDays, preferredSchools):
            super().__init__(fName, mName, lName, dateOfBirth, address, email)
            self.studentStatus = studentStatus
            self.mainGuardian = mainGuardian
            self.secondaryGuardian = secondaryGuardian
            self.schoolCurrEnrolled = schoolCurrEnrolled
            self.disabilityDetails = disabilityDetails
            self.availableDays = availableDays
            self.preferredSchools = preferredSchools
    
    def printStudentInfo(self):
        print("Name: ",self.firstName, self.middleName, self.lastName)
