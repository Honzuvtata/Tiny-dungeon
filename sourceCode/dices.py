import random

def D4():
    return random.randint(1, 4)

def D6():
    return random.randint(1, 6)

def D8():
    return random.randint(1, 8)

def D10():
    return random.randint(1, 10)

def D12():
    return random.randint(1, 12)

def D20():
    return random.randint(1, 20)

def checkSuccess(diceRolls):
    if 5 or 6 in diceRolls:
        return True
