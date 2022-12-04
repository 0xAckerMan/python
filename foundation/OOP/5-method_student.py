'''
Creating my own method inside the class called duty

if Duty is sweeping, it displays class
        mopping, dorm
        prefect, coordinate
        captain, supervise

'''
class Student:
    def __init__(self, name,house,role):
        self.name = name
        self.house = house 
        self.role = role

    def __str__(self):
        return f"Your name is {self.name} from {self.house}\n"

    def duty(self):
        if self.role =="sweeping":
            return "Sweeping class"
        elif self.role == "mopping":
            return "Mopping Dorm"
        elif self.role == "prefect":
            return "coordinator"
        elif self.role == "Captain":
            return "Supervision"
        else:
            return "Oh! oh! I dont know YOOUUU!!"

    
'''
Using match option with switch selection...Also works perfectly

    def Duty(self,role):
        match role:
            case  "Sweeping":
                return "Class"
            case "mopping":
                return "Dorm"
            case "prefect":
                return "coordinator"
            case "captain":
                return "supervise"
'''

def main():
    stude = get_student()
    print(stude)
    print(f"YOUR WORK IS: {stude.duty()}")

def get_student():
    name = input("What is your name? ")
    house = input("Where are you from? ")
    role = input("Whats ur role ")

    return Student(name,house,role)

if __name__ == "__main__":
    main()