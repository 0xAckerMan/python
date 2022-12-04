'''
Program has 3 functions
'''

def main():
    name = get_name()
    house = get_house()

    print(f"My name is {name} from {house}")

def get_name():
    return str(input("Whats your name? "))

def get_house():
    return input("Which house are you from? ")

if __name__ == "__main__":
    main()