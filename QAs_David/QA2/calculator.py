# Vi vill göra en miniräknare som tar uttryck på formen
# add 3 5
# och printar svaret (i detta fall 8)
# Om man skriver h skall en hjälptext printas 
# och om man skriver q ska programmet avslutas

def main():
    # Definiera hjälptexten 
    # trippeldubbelfnuttar gör en sträng som kan radbrytas
    helptext = """Type expressions of the form <operator> <operand> <operand> or
    h for help or q to quit"""

    for i in range(100):
        inputStr = input("What do you want to do (type h for help)? ")
        if len(inputStr) == 1:
            if inputStr == "h":
                print(helptext)
            elif inputStr == "q":
                break
            else:
                print("Invalid operation")
        else:
            # Denna del kan göras mycket smidigare med dictionaries,
            # (grov) överkurs övning är att skriva om den med
            # operators som en dictionary istället för en lista med tuplar

            operators = [("add", add),
                         ("subtract", subtract),
                         ("multiply", multiply),
                         ("divide", div)]

            inputOp, x, y = inputStr.split(" ")

            for string, operator in operators:
                if inputOp == string:
                    print(operator(float(x), float(y)))
                    break
            else:  # Ingen sträng i operators matchade inputen
                print("Invalid op")
    
    # forloop slut
    print("Okay, byye :)")


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def div(x, y):
    return x/y


main()
