# Write a program to determine the length of a ladder required to reach a given
# heigth when leaned against a house. The heigth and angle of the ladder are given
# as inputs.

from math import *
import sys

#Tar höjd och vinkel (i radianer) som input, retunerar vilken längd vår stege behöver ha!
def ladderLength(h, v):
    return h/sin(v)

#tar input från använadren då ladder.py körs
def oldMain():
    h = float(input("Ange husets höjd: "))
    v = int(input("Ange vinkel i grader: "))
    v = radians(v)
    print("Stegen måste vara ", ceil(ladderLength(h,v)), " meter lång.")

#tar input direkt från "command line"
def main():
    print("sys.argv: ", sys.argv)
    h = float(sys.argv[1])
    v = radians(int(sys.argv[2]))
    print("Stegen måste vara ", ceil(ladderLength(h,v)), " meter lång.")

if __name__ == "__main__":
    main()
