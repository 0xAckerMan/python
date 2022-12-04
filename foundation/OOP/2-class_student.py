'''
Introduction to classes in python.
'''

class Student:
    ...

def main():
    student = get_student()
    print(f'You are {student.name} from {student.house}')

def get_student():
    stude = Student()
    stude.name = input("What is your name? ")
    stude.house = input("Where are you from? ")
    return stude

if __name__ == "__main__":
    main()