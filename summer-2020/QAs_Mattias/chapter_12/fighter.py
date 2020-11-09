class Fighter:
    def __init__(self, name):
        self._name = name
        self._max_health = 100
        self._health = self._max_health
        self._damage = 20
        self._potions = 2
        self._magic_resistance = 0
        self._armor = 0

    def get_health(self):
        return self._health

    def get_name(self):
        return self._name

    # Set health to an appropriate value
    def set_health(self, new_health):
        if new_health >= self._max_health:
            self._health = self._max_health
        elif new_health < 0:
            self._health = 0
        else:
            self._health = round(new_health)

    def attacked_status(self):
        if self._health <= 0:
            print(self._name, 'died.')
        else:
            print(self._name, 'has', self._health, 'health points.')

    # Attack an opponent
    def punch(self, opponent):
        """:type opponent: Fighter"""
        print(self._name, 'punched', opponent._name + '!')
        damage = self._damage
        opponent.set_health(opponent._health - (damage - opponent._armor) if opponent._armor < damage else
                            opponent._health - 1)
        opponent.attacked_status()

    # Heal yourself with a potion!
    def drink_potion(self):
        if self._potions > 0:
            self._potions -= 1
            self.set_health(self._health + 50)
            print(self._name, 'healed for 50 health points. ' + self._name + ' now has '
                  + str(self._potions) + ' potions.')
            print(self._name, 'has', self._health, 'health.')
        else:
            print(self._name, 'tried to heal but has no potions.')

    # Chooses what action to perform (heal, punch)
    def choose_action(self, opponent, action):
        action = action.split()
        if action[0].lower() == "heal":
            self.drink_potion()
        elif action[0].lower() == "punch":
            self.punch(next(opp for opp in opponent if opp.get_name().lower() == action[1].lower()))


# 'Mage' takes 'Fighter' as a parameter and uses its functions by inheritance
class Mage(Fighter):
    def __init__(self, name):
        Fighter.__init__(self, name)
        self._magic_damage = 20
        self._mana = 100
        self._magic_resistance = 0.5
        self._max_health = 80
        self._health = self._max_health

    def mana_status(self):
        self._mana -= 50
        print(self._name, 'has', self._mana, 'mana.')

    # Attacks all enemies
    def flame_blast(self, opponent):
        if self._mana > 0:
            output_string = self._name + ' cast flame blast on '
            if isinstance(opponent, Fighter):
                opponent = [opponent]
            for i in range(len(opponent)):
                opponent[i].set_health(
                    opponent[i]._health - self._magic_damage * (1 - opponent[i]._magic_resistance))
                output_string += opponent[i]._name + ', ' if i < len(opponent) - 1 else opponent[i]._name + '!'
            print(output_string)
            for i in range(len(opponent)):
                opponent[i].attacked_status()

            self.mana_status()
        else:
            print(self._name, 'tried to use flame blast but has insufficient mana.')

    # Stronger attack on single target
    def lightning_strike(self, opponent):
        """:type opponent: Fighter"""

        if self._mana > 0:
            print(self._name, 'cast lightning strike on', opponent._name + '!')
            damage = self._magic_damage * 3
            opponent.set_health(opponent._health - damage * (1 - opponent._magic_resistance))
            opponent.attacked_status()
            self.mana_status()
        else:
            print(self._name, 'tried to use lightning strike but has insufficient mana.')

    # Adds more possible actions
    def choose_action(self, opponent, action):
        super(Mage, self).choose_action(opponent, action)
        action = action.split()
        if action[0].lower() == "flame" and action[1].lower() == "blast":
            self.flame_blast(opponent)
        elif action[0].lower() == "lightning" and action[1].lower() == "strike":
            self.lightning_strike(next(opp for opp in opponent if opp.get_name().lower() == action[2].lower()))
