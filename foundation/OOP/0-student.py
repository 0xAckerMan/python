'''
Using a tuple to return students info
 
The code can be written in many ways, buut I am just showcasing two ways
'''


def main():
    student = get_student()

    print(f"Your name is {student[0]} from {student[1]}")

def get_student():
    n = input("Whats your name? ")
    h = input("Where are you from? ")
    return (n,h)

if __name__ == "__main__":
    main()


'''
def main():
    name, house = get_student()
    print(f"You are {name} from {house}")

def get_student():
    n = input("Whats your name? ")
    h = input("Where are you from? ")
    return (n,h)

if __name__ == "__main__":
    main()
'''