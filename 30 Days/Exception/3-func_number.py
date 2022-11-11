def main():
    num = get_int()
    print(f'x is {num}')

def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        
        except ValueError:
            print("x is not an integer")

        else:
            break
    return x

main()