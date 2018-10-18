from random import randint

print("DiceRoll - Jesper Andersson")
print("Enter the amount of dice to be rolled:")
diceAmount = int(input())

for i in range(diceAmount):
    print(randint(1, 6), end=' ')

#Old broken code:
#if diceAmount == 1:
#    print(diceRoll)
#else:
#    if diceAmount == 2:
#        print(diceRoll, diceRoll)
#    else:
#        if diceAmount == 3:
#            print(diceRoll, diceRoll, diceRoll)
#        else: SystemExit