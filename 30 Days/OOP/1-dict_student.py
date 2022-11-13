'''
using dictionary to get and return a studets details
'''


def main():
    student  = get_student()
    print(f"You are {student['name']} from {student['house']}")

def get_student():
    student = {}
    student['name'] = input('what\'s your name? ')
    student['house'] = input('where are you from? ')

    return student


if __name__ == "__main__":
    main()