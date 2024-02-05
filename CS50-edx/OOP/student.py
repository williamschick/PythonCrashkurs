class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city


def main(): 
    student = get_student()

    print(f"{student.name} from {student.city}")


def get_student():
    name = input("Name:")
    city = input("City:")

    return Student(name, city)


if __name__ == "__main__":
    main()