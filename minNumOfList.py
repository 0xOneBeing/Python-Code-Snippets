x = [12, 43, 4, 1, 6, 343, 10, 34, 12, 93, 783, 330, 896, 1, 55]

num = 0
min = 0

for items in x:
    if (num > items):
        min += items
        print(min)
    elif (num < items):
        min += num
        print(min)
print(min)
