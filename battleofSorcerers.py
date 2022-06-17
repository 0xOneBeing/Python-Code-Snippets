gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

gandalfWins = 0
sarumanWins = 0
tie = 0

for g in range(0, len(gandalf)):
    for s in range(0, len(saruman)):
        if (gandalf[g] > saruman[s]):
            print("Gandalf wins!")
            gandalfWins += 1
        elif (gandalf[g] < saruman[s]):
            print("Saruman wins!")
            sarumanWins += 1
        else:
            print("Tie!")
            tie += 1
        s += 1
    g += 1
print("\nGandalf won:",gandalfWins,"times while Saruman won:",sarumanWins,"times with",tie,"ties in all.")
