name = input('Enter your name: ')

file = open('name0.txt', 'a')
file.write(f'{name}\n')
file.close