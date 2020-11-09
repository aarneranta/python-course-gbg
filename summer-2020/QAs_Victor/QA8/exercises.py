#From QA session 8 
#Example class student
class Student:
    def __init__(self,name,age):
        self._name=name #instance variable
        self._age=age
        self._sex="male"
        self._rename()

    def getName(self): #accessor
        return self.name

    def setName(self,name): #mutator
        self.name=name

    def _rename(self):
        self.name=self.name.lower()


def student_class_example():
    student=Student("Pelle",33)
    name=student.getName()
    print(name)
    student._name="per" ## Do not do this!
    student.setName("per)") # Do this!

student_class_example()

from button import Button
from graphics import *
import random

def three_button_monte():
    # Graphics library reference (Good to know for lab2):
    #https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html
    #

    #create new window with our own defined coordinate system.
    win = GraphWin("Three Button Monte",200,200)
    win.setCoords(0,4,4,0)

    #create buttons "compactly" instead of b1=Button(..).., b2=Button(..).. etc..
    buttons=[Button(win,Point(i,1),1,1,"Button "+str(i)) for i in range(1,4)] # range(1,4) == [1,2,3]
    [b.activate() for b in buttons]

    #Chose 1 of the buttons randomly
    winner = random.choice(buttons)

    #Keep track of wins and losses
    num_wins=0
    num_losses=0

    #display win/loss counter
    wins=Text(Point(2,2),"wins: 0").draw(win)
    losses=Text(Point(2,3),"losses: 0").draw(win)

    #Initialize to None object.
    player_chose=None

    #Loop until player quits
    while True:
        #print(winner.getLabel()) # Debug, see which button is the winner
        click = win.getMouse()
        if buttons[0].clicked(click):
            player_chose=buttons[0]
        elif buttons[1].clicked(click):
            player_chose=buttons[1]
        elif buttons[2].clicked(click):
            player_chose=buttons[2]
        if player_chose == winner:
            num_wins+=1
            wins.setText("wins: " + str(num_wins))
        else:
            num_losses+=1
            losses.setText("losses: " + str(num_losses))

        winner = random.choice(buttons)

    win.getMouse()

three_button_monte()
