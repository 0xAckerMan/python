with open('name1.txt') as text:
    for line in sorted(text):
        print(f'Hello, {line.rstrip()}')
