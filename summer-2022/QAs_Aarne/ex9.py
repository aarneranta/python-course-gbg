# bank account

class Account:
    def __init__(self, number, balance):
        self._number = number
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self,b):
        self._balance = b

        
def transfer(account1,account2,amount):
    balance1 = account1.get_balance()
    balance2 = account2.get_balance()
    
    if 0 < amount <= balance1:   
        account1.set_balance(balance1 - amount)
        account2.set_balance(balance2 + amount)
        print('OK')
    else:
        print("not enough money")



# class for chess boards of different colours and sizes

from graphics import *

class Chessboard:
    def __init__(self, black, white, size):
        self._win = GraphWin('Schackbrädet', size*8, size*8)
        self._black = black
        self._white = white
        self._size = size

    def draw(self):
        size = self._size
        for y in range(8):
            for x in range(8):
                r = Rectangle(Point(x*size, y*size), Point((x+1)*size, (y+1)*size))

                # a square is white if both x and y are either even or odd
                if x % 2 == y % 2:
                    r.setFill(self._white)
                else:
                    r.setFill(self._black)
                r.draw(self._win)
        
# to test from OS command line
if __name__ == '__main__':
     Chessboard('brown','yellow',100).draw()
     input('press a key to go to the next question')


# class for targets of different colours and numbers of circles

class Target:
    def __init__(self, black, white, size):
        self._black = black
        self._white = white
        self._size = size
        self._circles = []  # save circle list to enable undraw()

    def draw(self, win):
        self.undraw()  # remove the old target before drawing a new one
        mid = Point(200, 200)
        for r in range(self._size):
            c = Circle(mid, 200-r*(200/self._size))
            if r % 2 == 0:
                c.setFill(self._black)
            else:
                c.setFill(self._white)
            c.draw(win)
            self._circles.append(c)  # save the circle to enable undraw()
            
    def undraw(self):
        for c in self._circles:
            c.undraw()
        

if __name__ == '__main__':
    win = GraphWin('Target',400,400)
    target = Target('orange','black',7)
    target.draw(win)
    input('press a key to show the next target')
    target.undraw()
    target = Target('green','white',10)
    target.draw(win)
    input('press a key to quit')

