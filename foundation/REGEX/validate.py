'''
For validating user emails from their input

A simple implementation that just uses if to check for @ and . in a domain
'''

def email_checker():
    email = input("Enter your email ").strip()
    user, domain = email.split("@")

    if user and domain.endswith(".com"):
        print ("Valid")
    else:
        print ("Invalid") 

email_checker()