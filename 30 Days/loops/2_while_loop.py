'''
Takes a user input(n) and prints n meows
n - must be positive
'''

def main():
    no = number ()
    meow(no)

def number():

	while True:
		n = int(input("what is number(n)? "))
		if n > 0:
			break

		return n

def meow():
	for _ in range (n):
		print ('meow')

main()
