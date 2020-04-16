from objects import *

def main_menu():
    print("*****TUTORING MANAGEMENT SYSTEM*****")
    print("1. View Students List")
    print("2. Add New Student")
    print("3. View Guardians List")
    print("4. Add New Guardian")
    print("5. View Tutors List")
    print("6. Add New Tutors")
    print("7. View Student-Tutor Matches")
    while True:
        option = int(input("Type the menu number form the list above or 0 to exit: "))
        if option == 1:
            listStudents()
        elif option == 2:
            addStudent()
        elif option == 3:
            searchGuardians()
        elif option == 4:
            addGuardian()
        elif option == 5:
            listTutors()
        elif option == 6:
            addTutor()
        elif option == 7:
            listMatches()
        elif option == 0:
            print("Exiting the program. See you next time!")
            break
        else:
            print("Not a valid option. Please try again.")

def addStudent():
    print("**********Warning**********")
    print("The student's guardian must be registered before add the new Student!")
    option = input("Please enter below the Student's information or enter \"cancel\" to return: ")
    if option.lower() == "cancel":
        main_menu()
    else:
        firstName = input("First Name: ")
        lastName = (input("Last Name: "))
        email = (input("Email: "))
        guardianToSearch = input("Enter the Guardian First or Last Name to search: (Press enter to list all Guardians)")
        searchGuardians(guardianToSearch)
        guardianId = input("Enter the Guardian ID from the list above: ")
        gradeLevel = input("Grade level: ")
        listSubjects()
        subjectId = input("Enter the Subject ID from the list above: ")
        st = Student(firstName,lastName,email,guardianId,gradeLevel,subjectId)
        print(st)
        confirmInput = input("The student above will be added. Press Enter to confirm or type \"cancel\" to return.")
        if confirmInput.lower() == "cancel":
            print("New Student not added.")
            main_menu()
        else:
            st.commitStudent()
            print("New Student successfully added.")
            
def addGuardian():
    option = input("Please enter below the Guardian's information or enter \"cancel\" to return: ")
    if option.lower() == "cancel":
        main_menu()
    else:
        firstName = input("First Name: ")
        lastName = (input("Last Name: "))
        email = (input("Email: "))
        guardianType = (input("Guardian type: "))
        isMainContact = (input("Is the guardian the main contact with the student (yes/no): "))
        gd = Guardian(firstName,lastName,email,guardianType,isMainContact)
        print(gd)
        confirmInput = input("The Guarduan above will be added. Press Enter to confirm or type \"cancel\" to return.")
        if confirmInput.lower() == "cancel":
            print("New Guardian not added.")
            main_menu()
        else:
            gd.commitGuardian()
            print("New Guardian successfully added.")
            
def addTutor():
    option = input("Please enter below the Tutor's information or enter \"cancel\" to return: ")
    if option.lower() == "cancel":
        main_menu()
    else:
        firstName = input("First Name: ")
        lastName = (input("Last Name: "))
        email = (input("Email: "))
        minGradeLevel = (input("Min grade level to teach: "))
        maxGradeLevel = (input("Max grade level to teach: "))
        listSubjects()
        subjectId = input("Enter the Subject ID from the list above: ")
        tt = Tutor(firstName,lastName,email,minGradeLevel,maxGradeLevel,subjectId)
        print(tt)
        confirmInput = input("The Tutor above will be added. Press Enter to confirm or type \"cancel\" to return.")
        if confirmInput.lower() == "cancel":
            print("New Tutor not added.")
            main_menu()
        else:
            tt.commitTutor()
            print("New Tutor successfully added.")            
        
        
    
    
        
                
