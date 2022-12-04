import re

def main():
    return email_checker()

def email_checker():
    email = input("Enter your email: ")

    if re.search("@" and ".com", email):
        print ("vaild")
    else:
        print("Invalid")

main()