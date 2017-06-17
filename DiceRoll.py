# Random number generation between 1-6
from random import randint

print("Type in 'roll' to roll the dice...")
rollprompt = raw_input()

if rollprompt == "roll":
    print(randint(1, 6), randint(1, 6))
else:
    raise SystemExit
