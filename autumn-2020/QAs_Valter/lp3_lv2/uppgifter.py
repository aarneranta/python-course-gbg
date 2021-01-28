# Uppgift 1
class Dish:
    def __init__(self, type, name, cost):
        self.type = type
        self.name = name
        self.cost = cost

    def get_cost(self, cost):
        return self.cost


# Uppgift 2
class Dish:
    def __init__(self, type, name, cost):
        self.type = type
        self.name = name
        self.cost = cost

    def get_cost(self, cost):
        return self.cost

    def __str__(self):
        return f"The {self.type} dish {self.name} costs ${self.cost}"


# Uppgift 3
class Course:
    def __init__(self, dishes):
        self.price = price
        self.dishes = dishes

    def __str__(self):
        return (
            "\n".join(str(dish) for dish in self.dishes)
            + f"\nTotal cost: {sum(dish.price for dish in self.dishes)}"
        )


# Uppgift 4
class Course:
    def __init__(self, dishes):
        self.price = price
        self.dishes = dishes

        if len(dishes) != 3:
            print("Not three dishes!")

        types = set(dish.type for dish in dishes)
        if types != set("starter", "main", "dessert"):
            print("This is a strange course! Are you sure this is right?")

    def __str__(self):
        return (
            "\n".join(str(dish) for dish in self.dishes)
            + f"\nTotal cost: {sum(dish.price for dish in self.dishes)}"
        )


# Uppgift 5
class Player:
    def __init__(self, name, health, attack_strength):
        self.name = name
        self.health = health
        self.attack_strength = attack_strength

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} DMG. Health now at {self.health} HP")

    def drink_potion(self, potion_strength):
        self.health += potion_strength
        print(f"{self.name} drank a potion for {potion_strength} HP")

    def __str__(self):
        return f"{self.name} at {self.health} HP and {self.attack_strength} attack strength"


# Uppgift 6
class Duel:
    def __init__(self, player1, player2):
        self.current_player, self.other_player = player1, player2
        self.game_over = False

        print("Duel started!")
        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")

    def turn(self):
        self.other_player.take_damage(self.current_player.attack_strength)
        if self.other_player.health <= 0:
            print(f"{self.current_player.name} won!")
            self.game_over = True

        self.current_player, self.other_player = self.other_player, self.current_player

    def play(self):
        while True:
            self.turn()
            if self.game_over:
                break


# Uppgift 7, gör det själv mer intressant m.h.a random-modulen!
