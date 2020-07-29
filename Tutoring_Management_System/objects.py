from abc import ABCMeta
import sqlite3
from contextlib import closing
import TableIt #source: https://github.com/CodeForeverAndEver/TableIt


DB_FILE = "C:/Users/rafon/Documents/GBC/COMP2152_Python/Database/sqlite/tutoringManagementSystem.sqlite3"
conn = sqlite3.connect(DB_FILE)

def searchGuardians(name=""):
    with closing(conn.cursor()) as c:
        query = '''SELECT guardian_id, first_name, last_name, email, guardian_type, is_main_contact 
                    FROM Guardians
                    WHERE upper(first_name) LIKE upper("%{}%")
                    OR upper(last_name) LIKE upper("%{}%");'''
        c.execute(query.format(name, name))
        guardians = c.fetchall()
        if guardians[0] is not None:
            guardiansList = [["Guardian ID","First name","Last Name","Email","Type","Is Main Contact?"]]
            for guardian in guardians:
                guardiansList.append([guardian[0],guardian[1],guardian[2],guardian[3],guardian[4],guardian[5]])
            print("**************GUARDIANS LIST**************")
            TableIt.printTable(guardiansList, useFieldNames=True)
        else:
            print("No results found.")

def listSubjects():
    with closing(conn.cursor()) as c:
        query = '''SELECT subject_id, subject_name
                    FROM Subjects;'''
        c.execute(query)
        subjects = c.fetchall()
        if subjects[0] is not None:
            subjectsList = [["Subject ID","Subject name"]]
            for subject in subjects:
                subjectsList.append([subject[0],subject[1]])
            print("\n****************************SUBJECTS LIST****************************")
            TableIt.printTable(subjectsList, useFieldNames=True)
        else:
            print("No subjects were found.")
            
def listStudents():
    with closing(conn.cursor()) as c:
        query = '''SELECT DISTINCT Students.student_id,
                        Students.first_name, 
                        Students.last_name, 
                        Students.email, 
                        Students.grade_level, 
                        Guardians.First_Name || ' ' || Guardians.Last_Name as "Guardian Name",
                        Subjects.subject_name
                    FROM Students
                    LEFT JOIN Family ON Family.student_id = Students.student_id
                    LEFT JOIN Guardians ON Family.guardian_id = Guardians.guardian_id
                    LEFT JOIN Subjects ON Subjects.subject_id = Students.subject_id;'''
        c.execute(query)
        students = c.fetchall()
        if students is not None:
            studentsList = [["Student ID","First name", "Last name", "Email", "Grade Level", "Guardian Name", "Subject for Help"]]
            for student in students:
                studentsList.append([student[0],student[1],student[2],student[3],student[4],student[5],student[6]])
            print("\n****************************SUBJECTS LIST****************************")
            TableIt.printTable(studentsList, useFieldNames=True)
        else:
            print("No subjects were found.")
            
def listTutors():
    with closing(conn.cursor()) as c:
        query = '''SELECT tutor_id,
                        first_name, 
                        last_name, 
                        email, 
                        min_grade_level, max_grade_level, 
                        Subjects.subject_name
                    FROM Tutors
                    LEFT JOIN Subjects ON Tutors.subject_id = Subjects.subject_id;'''
        c.execute(query)
        tutors = c.fetchall()
        if tutors is not None:
            tutorsList = [["Tutor ID","First name", "Last name", "Email", "Grade Level Range", "Subject"]]
            for tutor in tutors:
                tutorsList.append([tutor[0],tutor[1],tutor[2],tutor[3],(str(tutor[4])+"-"+str(tutor[5])),tutor[6]])
            print("\n****************************TUTORS LIST****************************")
            TableIt.printTable(tutorsList, useFieldNames=True)
        else:
            print("No subjects were found.")            

def listMatches():
    with closing(conn.cursor()) as c:
        query = '''SELECT Students.student_id, 
            		Students.first_name||' '||Students.last_name AS "Student Name",
                    Students.grade_level,
                    Subjects.subject_name,
                    Tutors.first_name||' '||Tutors.last_name AS "Tutor Name",
                    Tutors.min_grade_level||'-'||Tutors.max_grade_level AS "Grade Level Range",
                    Subjects.subject_name
                  FROM Students
                  LEFT JOIN Subjects on Subjects.subject_id = Students.subject_id
                  LEFT JOIN Tutors on Subjects.subject_id = Tutors.subject_id
                  WHERE Students.grade_level >= Tutors.min_grade_level 
                      AND Students.grade_level <= Tutors.max_grade_level
                      AND Students.subject_id LIKE Tutors.subject_id;'''
        c.execute(query)
        matches = c.fetchall()
        if matches is not None:
            matchesList = [["Student ID","Student name", "Grade Level", "Subject","Tutor Name", "Grade Level Range", "Subject"]]
            for match in matches:
                matchesList.append([match[0],match[1],match[2],match[3],match[4],match[5],match[6]])
            print("\n****************************MATCHES LIST****************************")
            TableIt.printTable(matchesList, useFieldNames=True)
        else:
            print("No matches were found.")

#Get last used ID from Database and return next available ID
def getNewId(personId, tableName):
        with closing(conn.cursor()) as c:
            query = '''SELECT MAX({}) FROM {};'''
            c.execute(query.format(personId,tableName))
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
    def __init__(self, fName, lName, email, guardianType, isMainContact):
            super().__init__(fName, lName, email)
            self.guardianId = getNewId("guardian_id","Guardians")
            self.guardianType = guardianType
            self.isMainContact = isMainContact
            
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
        output = "Guardian ID: {}\nFirst Name: {}\nLast Name: {}\nEmail: {}\nType {}\nMain Contact: {}".format(
            self.guardianId,
            self.firstName, 
            self.lastName,
            self.email,
            self.guardianType,
            self.isMainContact
        )
        return output

#Student Class
class Student(Person):
        
    def __init__(self, fName, lName, email, guardian, 
        gradeLevel, subjectForHelp):
            super().__init__(fName, lName, email)
            self.studentId = getNewId("student_id","Students")
            self.gradeLevel = gradeLevel
            self.guardian = guardian
            self.subjectForHelp = subjectForHelp
    
    def commitStudent(self):
        with closing(conn.cursor()) as c:
            query1 = '''INSERT INTO "main"."Students"(
                         "first_name","last_name","email","grade_level","subject_id") 
                    VALUES (?,?,?,?,?);'''
            c.execute(query1, 
                   (self.firstName,
                   self.lastName,
                   self.email,
                   self.gradeLevel,
                   self.subjectForHelp))
            conn.commit()
            query2 = '''INSERT INTO "main"."Family"(
                         "student_id","guardian_id") 
                    VALUES (?,?);'''
            c.execute(query2, 
                   (self.studentId,
                   self.guardian,))
            conn.commit()
            

    def __str__(self):
        output = "ID: {}\nFirst Name: {}\nLast Name: {}\nEmail: {}\nGrade Level: {}\nGuardian ID: {}\nSubject for help: {}".format(
            self.studentId,
            self.firstName, 
            self.lastName, 
            self.email, 
            self.gradeLevel,
            self.guardian,
            self.subjectForHelp
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
                         "first_name","last_name","email","min_grade_level", "max_grade_level","subject_id") 
                    VALUES (?,?,?,?,?,?);'''
         c.execute(query, 
                   (self.firstName,
                   self.lastName,
                   self.email,
                   self.minGradeLevel,
                   self.maxGradeLevel,
                   self.subjectToHelp))
         conn.commit()
    
    def __str__(self):
        output = "Tutor Id: {}\nFirst Name: {}\nLast Name: {}\nEmail: {}\nMin Grade Level: {}\nMax Grade Level: {}\nSubject: {}".format(
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