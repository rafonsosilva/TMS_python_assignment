def main_menu():
    print("*****TUTORING MANAGEMENT SYSTEM*****")
    print("1. Work with Students")
    print("2. Work with Parents")
    print("3. Work with Tutors")
    print("3. Work with Schools")
    print("4. List Students-Tutors Matches")
    while True:
        option = int(input("Option: "))
        if option == 1:
            students_menu()
            break
        else:
            print("Not a valid option. Please try again.")

def students_menu():
    print("*****STUDENTS MENU*****")
    print("1. Add Student")
    print("2. Edit Student Info")
    while True:
        option = int(input("Option: "))
        if option == 1:
            students_menu()
            break
        else:
            print("Not a valid option. Please try again.")

def add