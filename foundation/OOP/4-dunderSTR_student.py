'''
using the dunder str (__str__) to customize my print func in main
'''

class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"You are {self.name} from {self.house}"

def main():
    stude = get_student()
    print (stude)


def get_student():
    name = input("Enter ur name ")
    house = input("Where are u from ")
    return Student(name,house)

main()