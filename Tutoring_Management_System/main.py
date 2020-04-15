from objects import *
from functions import *
import datetime
import sqlite3
import sys
import os
from contextlib import closing

def main():
    # DB_FILE = "C:/Users/rafon/Documents/GBC/COMP2152_Python/Database/tms_database.db"
    # conn = sqlite3.connect(DB_FILE)
    
    # with closing(conn.cursor()) as c:
    #     query = '''SELECT Students.student_id,
	#                 Students.first_name, 
	#                 Students.last_name, 
	#                 Students.grade_level, 
	#                 Guardians.First_Name,
	#                 Guardians.last_name
    #             FROM Students
	#                 INNER JOIN Family ON Family.student_id = Students.student_id
	#                 INNER JOIN Guardians ON Family.guardian_id = Guardians.guardian_id
    #             WHERE Students.student_id = 2;'''
    #     c.execute(query)
    #     student = c.fetchone()
    
    # print("Student id: "+str(student[0]))
    # print("Student name: "+str(student[1])+str(student[2]))

    main_menu()
    




if __name__ == "__main__":
    main()