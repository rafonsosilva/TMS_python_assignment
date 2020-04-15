from objects import Student, Guardian, Tutor, Subject
from functions import * 
import sqlite3
from contextlib import closing

#def getNewTutorId():
#         with closing(conn.cursor()) as c:
#             query = '''SELECT MAX(tutor_id) FROM "Tutors";'''
#             c.execute(query)
#             result = c.fetchone()
#             if result[0] is None:
#                 newId = 1
#             else:
#                 newId = result[0] + 1
#             
#             return newId


def main():
    DB_FILE = "C:/Users/rafon/Documents/GBC/COMP2152_Python/Database/tms_database.db"
    conn = sqlite3.connect(DB_FILE)

#     with closing(conn.cursor()) as c:
#         query = '''SELECT Students.student_id,
#	                 Students.first_name, 
#	                 Students.last_name, 
#	                 Students.grade_level, 
#	                 Guardians.First_Name,
#	                 Guardians.last_name
#                 FROM Students
#	                 INNER JOIN Family ON Family.student_id = Students.student_id
#	                 INNER JOIN Guardians ON Family.guardian_id = Guardians.guardian_id
#                 WHERE Students.student_id = 2;'''
#         c.execute(query)
#         student = c.fetchone()
#    
#     print("Student id: "+str(student[0]))
#     print("Student name: "+str(student[1])+str(student[2]))

    #main_menu()

#    s1 = Student("george", "silva", "george@gmail.com", "", "5", "Math","Monday")
#    s1.commitStudent()
#    s2 = Student("karl", "silva", "george@gmail.com", "", "5", "Math","Monday")
#    s2.commitStudent()
#    s3 = Student("mary", "silva", "george@gmail.com", "", "5", "Math","Monday")
#    s3.commitStudent()
#    s4 = Student("john", "silva", "george@gmail.com", "", "5", "Math","Monday")
#    s4.commitStudent()
    
#    g3 = Guardian("Nadia","Smith","ns@jt.com","mother","yes",(4,5,))
#    g3.commitGuardian()
#    g4 = Guardian("Jack","Hittherode","jh@mj.com","father","no",(3,6,))
#    g4.commitGuardian()

#    t1 = Tutor("Riordan","Daniel","rd@rd.com",5,8,("Math","English",),("Wednesday","Saturday",))    
#    t1.commitTutor()
#    
#    t2 = Tutor("Raquel","Arazaki","ra@ra.com",5,8,("Math","English",),("Wednesday","Saturday",))
#    t2.commitTutor()
    
    sub1 = Subject("Math")
    sub1.commitSubject()
    
    sub2 = Subject("English")
    sub2.commitSubject()
    
    sub3 = Subject("Science")
    sub3.commitSubject()
    print(sub1)
    print(sub2)
    print(sub3)
    
    
        
    
if __name__ == "__main__":
    main()