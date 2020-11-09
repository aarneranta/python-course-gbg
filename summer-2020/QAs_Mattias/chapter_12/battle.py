from QAs_Mattias.chapter_12.fighter import Fighter, Mage    # This is the folder where Fighter and Mage are located

# When the battle occurs, a Fighter can use punch and heal.
# To use punch, type "punch <name of opponent>".
# To use heal, just type heal.
# A Mage can in addition use flame blast and lightning strike.
# Flame blast attacks all opponents, just type "flame blast".
# Lightning strike attacks a single opponent, type "lightning strike <name of opponent>".
# Feel free to alter team1 and team2 below to make your own teams!

class Battle:
    def __init__(self, good_guys, bad_guys):
        self.good_guys, self.bad_guys = good_guys, bad_guys
        self.good_guys_turn = True
        self.good_player_nr = 0
        self.bad_player_nr = 0

    @staticmethod
    def increment_player_nr(persons, nr):
        if nr >= len(persons) - 1:
            return 0
        else:
            return nr + 1

    def next_turn(self):
        if self.good_guys_turn:
            self.good_guys_turn = False
            self.good_player_nr = Battle.increment_player_nr(self.good_guys, self.good_player_nr)
        else:
            self.good_guys_turn = True
            self.bad_player_nr = Battle.increment_player_nr(self.bad_guys, self.bad_player_nr)

    def this_turn(self):
        if self.good_guys_turn:
            print("It is the good guys' turn")
            print("It is", self.good_guys[self.good_player_nr].get_name() + "'s turn to attack.")
            action = input("Choose what action " + self.good_guys[self.good_player_nr].get_name() + " should take: ")
            self.good_guys[self.good_player_nr].choose_action(self.bad_guys, action)
        else:
            print("It is the bad guys' turn")
            print("It is", self.bad_guys[self.bad_player_nr].get_name() + "'s turn to attack.")
            action = input("Choose what action " + self.bad_guys[self.bad_player_nr].get_name() + " should take: ")
            self.bad_guys[self.bad_player_nr].choose_action(self.good_guys, action)

    def summary(self):
        print("Good guys:")
        for i in range(len(self.good_guys)):
            output = ' ' * 15 + self.good_guys[i].get_name() + \
                     ' has ' + str(self.good_guys[i].get_health()) + ' health points.'
            print(output)
        print("Bad guys:")
        for i in range(len(self.bad_guys)):
            output = ' ' * 15 + self.bad_guys[i].get_name() + \
                     ' has ' + str(self.bad_guys[i].get_health()) + ' health points.'
            print(output)
        print("_" * 50)

    @staticmethod
    def check_dead(team, nr):
        new_team = []
        new_nr = 0
        for i in range(len(team)):
            if team[i].get_health() > 0:
                new_team.append(team[i])
                if i <= nr:
                    new_nr = len(new_team) - 1
        return new_team, new_nr

    def battling(self):
        if len(self.good_guys) == 0:
            print("Bad guys win!")
            return False
        elif len(self.bad_guys) == 0:
            print("Good guys win!")
            return False
        else:
            return True

    def do_battle(self):
        while self.battling():
            self.summary()
            self.this_turn()
            self.good_guys, self.good_player_nr = Battle.check_dead(self.good_guys, self.good_player_nr)
            self.bad_guys, self.bad_player_nr = Battle.check_dead(self.bad_guys, self.bad_player_nr)
            self.next_turn()
            print("_" * 50)


merlin = Mage("Merlin")
team1 = [merlin]
johan = Fighter("Johan")
emil = Fighter("Emil")
nyarlathotep = Mage("Nyarlathotep")
team2 = [johan, emil, nyarlathotep]
battle = Battle(team1, team2)
battle.do_battle()
