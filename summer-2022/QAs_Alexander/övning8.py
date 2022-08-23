# -*- coding: utf-8 -*-
"""
Write a class to represent spheres, your class should implement the following methods:
    
    __init__(self, radius) Creates a sphere having the given radius
    getRadius(self) Returns the radius
    surfaceArea(self) Returns the surface area of the sphere
    volume(self) Returns the volume of this sphere
    
    Formulas:
        V = 4/3 * pi * r^3
        A = 4 * pi * r^2
"""
import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return 4*math.pi*self.radius**2
    
    def volume(self):
        return 4/3 * math.pi * self.radius**3
    

sph = Sphere(1)

print(sph.getRadius())
print(sph.surfaceArea())
print(sph.volume())


"""
Implement a class to represent a playing card. Your class should have the following
methods:
    __init__(self, rank, suit) rank is a int in the range 1-13 indicating the ranks
    of ace-king and suit is a single character "d", "c", "h", "s" indicating the suit.
    Create the corresponding card
    
    getRank(self) Returns the rank of the card
    getSuit(self) Returns the suit of the card
    
    value(self) Returns the blackjack value of a card. Ace counts as 1, face cards as 10
    
    __str__(self) Returns a string that names the card. E.g "Ace of spades"
    
    Test your class with a program that prints out n randomly generated cards 
    and their blackjack values
"""

import random

class Card:
    
    def __init__(self, rank, suit):
        ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.rank = ranks[rank-1]
        suits = {"d":"Diamond", "c":"Clove", "h":"Heart", "s":"Spade"}
        self.suit = suits[suit]
        
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank == "Ace":
            return 1
        elif self.rank == "Jack" or self.rank == "Queen" or self.rank == "King":
            return 10
        else:
            return self.rank
        
    def __str__(self):
        s = str(self.rank) + " of " + self.suit + "s"
        return s

n = 10
for i in range(n):
    r = random.randrange(1,13)
    suits = ["d", "c", "h", "s"]
    s = random.randrange(0,3)
    c = Card(r,suits[s])
    print(c)
    
#Diskutera lite varför vi gjorde card som en klass

