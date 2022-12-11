name = input('Enter your name: ')

with open('name1.txt', 'a') as text:
    text.write(f"{name} \n")