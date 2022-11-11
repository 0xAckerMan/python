def main():
    x = square("Enter a number ")
    print(f"The square is: {x}")

def square(prompt):
    while True:
        try:
            num = int(input(prompt))
            num = num**2
        except ValueError:
            print("input is not a number")
        else:
            return num

if __name__ == "__main__":
    main()