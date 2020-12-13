OWN_CASES = 28

def pandemic_rules(own, pop, cases):

    cases100k = 100000 * cases/pop
    
#    print(cases100k) # debug

    if cases100k < own:
        return 'green'
    elif cases100k < 25:
        return 'green'
    elif cases100k < 50:
        return 'yellow'
    else:
        return 'red'

#from a file
def pandemic_from_data(filename):
    file = open(filename)
    for line in file:
        tuple = line.split()
        if len(tuple) > 2:
            pop = int(tuple[1])
            
            if pop == 0:
                print("error: 0 population in",tuple[0])
                break
            else:
                pass
            
            cases = int(tuple[2])
            
            if pop < cases:
                print("warning: too many cases in",tuple[0])
                

            color = pandemic_rules(OWN_CASES, pop, cases)
            print(tuple[0], ":", color)
    
# interactive text
def apply_pandemic_rules(own):
    pop = int(input("Hur stor är ditt lands befolkning? "))
    cases = int(input("Hur många fall har ditt land haft? "))
    print("Ditt land är ", pandemic_rules(own,pop,cases))

# interactive graphic
from graphics import *
def graphic_pandemic_rules(own):

    win = GraphWin("Inreseregler", 500, 500)
    win.setBackground('cyan')

    textOwn = Text(Point(200,30), "I vårt land: " + str(own))
    textOwn.setSize(20)
    textOwn.draw(win)
    
    textPop = Text(Point(200,100), "Ditt lands befolkning")
    textPop.setSize(20)
    textPop.draw(win)
    inputPop = Entry(Point(400,100),10)
    inputPop.setText("10000000")
    inputPop.draw(win)

    textCases = Text(Point(200,200), "Antal fall i ditt land")
    textCases.setSize(20)
    textCases.draw(win)
    inputCases = Entry(Point(400,200),10)
    inputCases.setText("0")
    inputCases.draw(win)

    button = Rectangle(Point(200,300),Point(300,400))
    button.setFill('pink')
    button.draw(win)
    textButton = Text(Point(250,350),"Beslut")
    textButton.setSize(20)
    textButton.draw(win)
    
    win.getMouse()
    
    pop = int(inputPop.getText())
    cases = int(inputCases.getText())
    color = pandemic_rules(own,pop,cases)
    
    win.setBackground(color)
    textButton.setText("Avsluta")

    win.getMouse()
    win.close()

    
def main():
#    pandemic_from_data("/Users/aarne/Teaching/python-course-gbg/doctor/cases.tsv")
    graphic_pandemic_rules(OWN_CASES)

if __name__ == '__main__':
    main()





