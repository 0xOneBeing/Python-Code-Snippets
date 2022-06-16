num = int(input("Enter an integer number: "))

if num == 0:
    print("Number is zero which is neither even nor odd.")
elif num % 2 == 0:
    print("Number is even")
elif num % 2 == 1:
    print("Number is odd")
else:
    print("Undefined!")
