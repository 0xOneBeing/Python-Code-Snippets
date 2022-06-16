num = input("Enter an integer number: ")

try:
    intNum = int(num)
    if intNum == 0:
        print("Number is zero which is neither even nor odd.")
    elif intNum % 2 == 0:
        print(num, "is an even number")
    elif intNum % 2 == 1:
        print(num, "is an odd number")
except ValueError:
    print(num, "is not an integer number")
