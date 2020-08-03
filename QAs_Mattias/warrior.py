class Warrior:
    def __init__(self, name, health=100, damage=10, potions=2):
        self.name = name
        self.health = health
        self.damage = damage
        self.potions = potions

    # Attack an opponent
    def attack(self, opponent):
        print(self.name, 'attacked', opponent.name+'!')
        opponent.health -= self.damage
        if opponent.health <= 0:
            del opponent.health
            print(opponent.name, 'died.')
        else:
            print(opponent.name, 'has', opponent.health, 'health.')
        print('_' * 20)

    # Set health to an appropriate value
    def set_health(self, new_health):
        if 1 < new_health < 1000:
            self.health = new_health

    # Set damage to an appropriate value
    def set_damage(self, new_damage):
        if 1 < new_damage < 500:
            self.damage = new_damage

    # Heal yourself with a potion!
    def drink_potion(self):
        if self.potions > 0:
            self.potions -= 1
            self.set_health(self.health + 50)
            print(self.name, 'healed for 50 health points.')
            print(self.name, 'has', self.health, 'health.')
        else:
            print(self.name, 'tried to heal but has no potions.')
        print('_' * 20)


jonas = Warrior(name="Jonas", health=100, damage=140)
aarne = Warrior(name="Aarne", health=150, damage=90, potions=1)
aarne.attack(jonas)
jonas.attack(aarne)
aarne.drink_potion()
aarne.drink_potion()
jonas.attack(aarne)
