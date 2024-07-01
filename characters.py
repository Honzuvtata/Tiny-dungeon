import random
import dices

class GeneralCharacter:
    def __init__(self, name, hp, attack, dmg=1):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def perform_attack(self, other):
        attackRolls = []
        for i in range(0, self.attack):
            attackRolls.append(dices.D6())

        print(f"{self.name} rolls {attackRolls} for attack!")

        if any(x in attackRolls for x in [5, 6]):
            print(f"{self.name} hits {other.name} for {self.dmg} damage!")
            other.take_damage(self.dmg)
        else:
            print(f"{self.name} misses the attack on {other.name}!")

    def __str__(self):
        return f"{self.name}: HP={self.hp}, DMG={self.dmg}, ATTACK={self.attack}"
    

def fight(character1, character2):
    print(f"The fight between {character1.name} and {character2.name} begins!")
    
    while character1.is_alive() and character2.is_alive():
        character1.perform_attack(character2)
        character2.perform_attack(character1)

        print(character1)
        print(character2)
        print("-" * 30)

    if character1.is_alive():
        print(f"{character1.name} wins the fight!")
    elif character2.is_alive():
        print(f"{character2.name} wins the fight!")
    else:
        print("It's a draw! Both characters are down.")

character1 = GeneralCharacter(name="Warrior", hp=2, attack=2)
character2 = GeneralCharacter(name="Rogue", hp=2, attack=1)

fight(character1, character2)