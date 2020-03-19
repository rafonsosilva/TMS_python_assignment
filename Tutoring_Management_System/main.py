from class_student import Student
import datetime

def main():
    st = Student("Rafael", "Afonso", "Silva", datetime.datetime(1985, 9, 1),
        "5 Michael Power Place", "rafonso@gmail.com", "active",
        "John", "Mary", "School Name GBC", 5, ["Math, English"], True,
        False, "", "Saturday", ["Bloor Collegiate Institute"])
    st.printStudentInfo()


if __name__ == "__main__":
    main()