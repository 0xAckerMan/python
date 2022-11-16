'''
Writing my own code to try and take inputes from the student and check whether
he/she comes from either 4 houses (Payens, Eindehoven, Aggrey and Obama)

keyword introduced is: raise

still perfecting the code "Its breaky still"
'''

class Student:
    def __init__(self,name,house):
        
        self.name = name
        self.house = house

    def dorm(self):
        if self.house == "payens":
            return "You are a student"
            raise ValueError




def main():
    std = get_student()
    print(f"You are {std.name} from {std.house}")

def get_student():
    #name = input("What is your name? ")
    
    try:
        name = input("What is your name? ")
    except ValueError:
        print('Whats ur name???? ')
    
    while True:
        try:
            house = input("Where are you from? ") 
        except ValueError:
            print("Enter a valid house")
        else:
            break
    return Student(name,house)

if __name__ == "__main__":
    main()