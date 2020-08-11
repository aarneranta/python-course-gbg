from graphics import *

class C4Game():
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.reset()
    def nextplayer(self):
        return self.player
    def size(self):
        return self.width, self.height
    def winner(self):
        return self.end

    def reset(self):
        self.state = [None] * self.height
        for i in range(self.height):
            self.state[i] = [0] * self.width
        self.end = 0
        self.player = 1

    def add(self, j):
        if not (0 <= j < self.width):
            raise IndexError('Outside board')
        if self.state[self.height-1][j] != 0:
            raise ValueError('Column full')
        i = 0
        while self.state[i][j] != 0:
            i += 1
        self.state[i][j] = self.player
        self.player = 2 if self.player == 1 else 1
        #if self.player == 1:
        #    self.player = 2
        #else:
        #    self.player = 1
        self._checkwinner_coord(i,j)
        return (i,j)

    def _checkwinner_coord(self, i, j):
        # horizontal
        h = four_in_a_row(self.state[i])
        # vertical
        #tmp = []
        #for k in range(self.height):
        #    tmp.append(self.state[k][j])
        v = four_in_a_row(row[j] for row in self.state)
        # diagonal /
        dbck = min(i,j)
        dfwd = min(self.height-i,self.width-j)
        d1 = four_in_a_row(self.state[i+offset][j+offset] for offset in range(-dbck,dfwd))
        # diagonal \
        dbck = min(self.height-1-i,j)
        dfwd = min(i+1,self.width-j)
        d2 = four_in_a_row(self.state[i-offset][j+offset] for offset in range(-dbck,dfwd))

        # first not None value
        self.end = next(filter(None, [h,v,d1,d2]), self.end)

def four_in_a_row(it):
    last = None
    seen = 0
    for el in it:
        if el == last:
            seen += 1
        else:
            last = el
            seen = 1
        if seen >= 4:
            return last
    return None

class C4Graphics():
    def __init__(self):
        self.win = GraphWin('Connect 4', 640,480)
        self.win.setCoords(-320,-240,320,240)

        self.game = C4Game(9,7)
        width, height = self.game.size()
        self.board = Board(Point(-310,-220), Point(310,210), width, height)
        self.board.draw(self.win)

        self.label = Text(Point(0,-230), 'Connect 4')
        self.label.draw(self.win)

    def main(self):
        while True:
            pl = self.game.nextplayer()
            self.label.setText(f'Player {pl} to play.')

            coord = self.board.clicked(self.win.getMouse())
            if coord is None:
                continue
            try:
                coord = self.game.add(coord[1])
            except ValueError:
                continue
            self.board.set_token(coord[0],coord[1],pl)
            
            if self.game.winner() == 0:
                continue
            self.label.setText(f'Player {self.game.winner()} wins!')
            self.win.getMouse()
            self.game.reset()
            self.board.clear()

class Board():
    def __init__(self, p1, p2, width, height):
        self.width = width
        self.height = height

        # aspect ratio
        sidew = abs(p1.getX() - p2.getX())/width
        sideh = abs(p1.getY() - p2.getY())/height
        side = min(sidew,sideh)
        offw = (sidew - side)*width/2
        offh = (sideh - side)*height/2

        x1 = min(p1.getX(),p2.getX())+offw
        x2 = max(p1.getX(),p2.getX())-offw
        y1 = min(p1.getY(),p2.getY())+offh
        y2 = max(p1.getY(),p2.getY())-offh

        self.outer = Rectangle(Point(x1,y1), Point(x2,y2))
        self.outer.setFill('white')

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.side = side

        # lines
        self.lines = []
        xL = x1+side
        while xL < x2:
            self.lines.append(Line(Point(xL,y1), Point(xL,y2)))
            xL += side
        yL = y1+side
        while yL < y2:
            self.lines.append(Line(Point(x1,yL), Point(x2,yL)))
            yL += side

        # tokens
        self.tokens = []
        for i in range(height):
            self.tokens.append([])
            for j in range(width):
                self.tokens[i].append(Circle(Point(x1+(j+0.5)*side, y1+(i+0.5)*side), side*0.45))
                self.tokens[i][j].setFill('white')
                self.tokens[i][j].setOutline('white')

    def set_token(self, i, j, p):
        self.tokens[i][j].setFill(['white','red','yellow'][p])

    def clear(self):
        for row in self.tokens:
            for token in row:
                token.setFill('white')

    def draw(self, win):
        self.outer.draw(win)
        for line in self.lines:
            line.draw(win)
        for row in self.tokens:
            for token in row:
                token.draw(win)

    def clicked(self, p):
        x = p.getX()
        y = p.getY()
        if not (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2):
            return None
        return (int((y-self.y1)//self.side), int((x-self.x1)//self.side))

if __name__ == '__main__':
    C4Graphics().main()
