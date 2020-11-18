# 2.9.5 Does keywords make good variable names?

#Poor choice of variable name
def doMath_poor():

    str = input("Vilken operation vill du göra?")

    result = 0

    if str == "m":
        a, b = eval(input("Skriv två tal du vill multiplicera separerat med ett kommatecken"))
        result = a * b
    
    print("Resultat: " + str(result))

def doMath():

    operationInput = input("Vilken operation vill du göra?")

    result = 0

    if operationInput == "m":
        a, b = eval(input("Skriv två tal du vill multiplicera separerat med ett kommatecken"))
        result = a * b
    
    print("Resultat: " + str(result))

# Programming Exercise: 7.7.3
def grade(score):
    score = int(score)

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#Simultanious assignment 
def switch(alice, bob):

    print("Alice: ", alice)
    print("Bob: ", bob)

    trade = input("Ska Alice och Bob byta sina frukter? (y/n) ")

    if trade == "y":
        alice, bob = bob, alice

    print("Alice: ", alice)
    print("Bob: ", bob)

    return alice, bob