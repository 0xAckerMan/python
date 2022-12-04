from square import square

def main():
    test_sqaure()

def test_sqaure():
    if square(3) != 9:
        print("3 squared is not 9")
    elif square(10) != 100:
        print("10 squared is not 100")
    else:
        print ("code is perfect")

if __name__ == "__main__":
    main()