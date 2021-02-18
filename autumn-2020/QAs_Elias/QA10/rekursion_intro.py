import sys

def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n*factorial(n-1)

def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Flytta disk 1 från torn", from_rod, "till torn", to_rod)
        return
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Flytta disk", n, "från torn", from_rod, "till torn", to_rod)
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)
