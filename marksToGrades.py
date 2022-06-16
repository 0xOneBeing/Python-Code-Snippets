marks = float(input("Enter your marks: "))

if marks < 25:
    print("F")
elif marks <= 45:
    print("E")
elif marks <= 60:
    print("D")
elif marks <= 75:
    print("C")
elif marks <= 90:
    print("B")
else:
    print("A")
