'''
Implementation of our code using classes and objects just to do the same thing
'''


class Student:
    def __init__(self, name,house):
        self.name = name
        self.house = house


def main():
    std = get_student()
    print(f"You are {std.name} from {std.house}")

def get_student():
    name = input("Whats your name? ")
    house = input("Where are you from? ")
    return Student(name,house)


if __name__ == "__main__":
    main()