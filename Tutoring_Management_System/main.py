from objects import Student, Guardian, Address
import datetime

def main():
    guardAddress = Address("Carlos Olympio Tostes, 479", "", "Araraquara", "14807-210")
    stAddress = Address("5 Michael Power Place", "309", "Etobicoke", "M9A0A3")

    guard1 = Guardian("John", "", "Afonso", datetime.date(1956, 2, 29),
        guardAddress, "adao@fs.com", "father", "416-123-1234")

    guard2 = Guardian("Mary", "", "Silva", datetime.date(1960, 6, 23),
        guardAddress, "mary@fs.com", "mother", "416-123-1234")

    st = Student("Rafael", "Afonso", "Silva", datetime.date(1985, 9, 1),
        stAddress, "rafonso@gmail.com", "active",
        guard1, guard2, "School Name GBC", 5, ["Math, English"], True,
        False, "", "Saturday", ["Bloor Collegiate Institute"])
    print(st)


if __name__ == "__main__":
    main()