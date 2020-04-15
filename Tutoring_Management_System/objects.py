from abc import ABCMeta
import sqlite3
from contextlib import closing

DB_FILE = "C:/Users/rafon/Documents/GBC/COMP2152_Python/Database/tutoringManagementSystem.sqlite3"
conn = sqlite3.connect(DB_FILE)

#Get last used ID from Database and return next available ID
def getNewId(personId, tableName):
        with closing(conn.cursor()) as c:
            query = '''SELECT MAX({}) FROM {};'''
            c.execute(query.format(personId,tableName))
            #c.execute(query,(personId,tableName,))
            result = c.fetchone()
            if result[0] is None:
               newId = 1
            else:
                newId = result[0] + 1
        return newId

#Person Abstract Class
class Person(metaclass = ABCMeta):
    def __init__(self, fName, lName, email):
        self.firstName = fName
        self.lastName = lName
        self.email = email

#Guardian Class
class Guardian(Person):
    def __init__(self, fName, lName, email, guardianType, isMainContact, students_list):
            super().__init__(fName, lName, email)
            self.guardianId = getNewId("guardian_id","Guardians")
            self.guardianType = guardianType
            self.isMainContact = isMainContact
            self.students_list = students_list
            
    def commitGuardian(self):
        with closing(conn.cursor()) as c:
         query = '''INSERT INTO "main"."Guardians"(
                         "first_name","last_name","email","guardian_type","is_main_contact") 
                    VALUES (?,?,?,?,?);'''
         c.execute(query, 
                   (self.firstName,
                   self.lastName,
                   self.email,
                   self.guardianType,
                   self.isMainContact,))
         conn.commit()

    def __str__(self):
        output = "{} | {} | {} | {} | {} | {} | {}".format(
            self.guardianId,
            self.firstName, 
            self.lastName,
            self.email,
            self.guardianType,
            self.isMainContact,
            self.students_list[0]
        )
        return output

#Student Class
class Student(Person):
        
    def __init__(self, fName, lName, email, guardians, 
        gradeLevel, subjectsForHelp):
            super().__init__(fName, lName, email)
            self.studentId = getNewId("student_id","Students")
            self.gradeLevel = gradeLevel
            self.guardians = guardians
            self.subjectsForHelp = subjectsForHelp
    
    def commitStudent(self):
        with closing(conn.cursor()) as c:
         query = '''INSERT INTO "main"."Students"(
                         "first_name","last_name","email","grade_level") 
                    VALUES (?,?,?,?);'''
         c.execute(query, 
                   (self.firstName,
                   self.lastName,
                   self.email,
                   self.gradeLevel,))
         conn.commit()

    def __str__(self):
        output = "{} | {} | {} | {} | {}".format(
            self.studentId,
            self.firstName, 
            self.lastName, 
            self.email, 
            self.gradeLevel
        )
        return output

#Tutor Class
class Tutor(Person):
    def __init__(self, fName, lName, email, minGradeLevel, maxGradeLevel, subjectsList):
        super().__init__(fName, lName, email)
        self.tutorId = getNewId("tutor_id","Tutors")
        self.minGradeLevel = minGradeLevel
        self.maxGradeLevel = maxGradeLevel
        self.subjectToHelp = subjectsList
    
    def commitTutor(self):
        with closing(conn.cursor()) as c:
         query = '''INSERT INTO "main"."Tutors"(
                         "first_name","last_name","email","min_grade_level", "max_grade_level") 
                    VALUES (?,?,?,?,?);'''
         c.execute(query, 
                   (self.firstName,
                   self.lastName,
                   self.email,
                   self.minGradeLevel,
                   self.maxGradeLevel,))
         conn.commit()
    
    def __str__(self):
        output = "{} | {} | {} | {} | {} | {}".format(
            self.tutorId,
            self.firstName, 
            self.lastName,
            self.email,
            self.minGradeLevel,
            self.maxGradeLevel,
            self.subjectToHelp
        )
        return output

class Subject():
    def __init__(self, subjectName):
        self.subjectId = getNewId("subject_id","Subjects")
        self.subjectName = subjectName
    
    def commitSubject(self):
        with closing(conn.cursor()) as c:
         query = '''INSERT INTO "main"."Subjects"("subject_name") 
                    VALUES (?);'''
         c.execute(query,(self.subjectName,))
         conn.commit()
    
    def __str__(self):
        output = "{} | {}".format(self.subjectId,self.subjectName)
        return output