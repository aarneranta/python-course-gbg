

# Write a program that plays fizz buzz up to a number the user picks.
# Fizz buzz is played by counting up from the number 1.
# If a number is divisible by 3 it's replaced by fizz.
# If it's divisible by 5 it's replaced by buzz.
# And if it's divisible by both it's replaced by fizz buzz.
# After program works with 3 and 5 add functionality for more numbers.


# går att göra detta i main men har en separat funktion för senare
def userInput():
    argument = int(input("How far should I count? "))
    return argument


# en första lösning som endast löser basfallet
# inte särskilt skalbar som tillägget av 7 visar
def process1(endpoint):
    for x in range(1, endpoint+1):
        if x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
            print("fizz buzz wuzz")
        elif x % 3 == 0 and x % 5 == 0:
            print("fizz buzz")
        elif x % 3 == 0 and x % 7 == 0:
            print("fizz wuzz")
        elif x % 5 == 0 and x % 7 == 0:
            print("buzz wuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        elif x % 7 == 0:
            print("wuzz")
        else:
            print(x)


# kontrollerar om num är delbar med 3, 5, 7 eller 11
def isDivisble1(num):
    if num % 3 == 0:
        return True
    elif num % 5 == 0:
        return True
    elif num % 7 == 0:
        return True
    elif num % 11 == 0:
        return True
    else:
        return False


# en andra lösning som sammanfogar flera fraser för att skapa den slutgiltiga frasen
# detta kräver en kontroll av om x är delbart eller inte för att avgöra om frasen eller talet ska skrivas ut
# denna funktion har bättre skalbarhet än den förra men man måste ändra på två ställen i koden
def process2(endpoint):
    for x in range(1, endpoint + 1):
        result = ""
        if x % 3 == 0:
            result = result + fizzword(3)
        if x % 5 == 0:
            result = result + fizzword(5)
        if x % 7 == 0:
            result = result + fizzword(7)
        if x % 11 == 0:
            result = result + fizzword(11)
        if isDivisble1(x):
            print(result)
        else:
            print(x)


# använder en avancerad for loop för att avgöra om num är delbar av någon delare
def isDivisble2(num):
    for divisor in divisorList():
        if num % divisor == 0:
            return True
    return False


# översätter en delare till dess associerade fras
def fizzword(num):
    if num == 3:
        return "fizz "
    elif num == 5:
        return "buzz "
    elif num == 7:
        return "wuzz "
    elif num == 11:
        return "tazz "
    elif num == 13:
        return "jyzz "
    else:
        return ""


# generar en list av alla delare
def divisorList():
    return [3, 5, 7, 11, 13]


# denna lösning använder en avancerad for loop för att generalisera delbarhets kontrollen
def process3(endpoint):
    for x in range(1, endpoint + 1):
        result = ""
        # avancerad for loop som utför nedanstående för alla tal i listan
        for divisor in divisorList():
            if x % divisor == 0:
                result = result + fizzword(divisor)
        if isDivisble2(x):
            print(result)
        else:
            print(x)


def main():
    argument = userInput()
    # ändra processfunktionen som kallas för att köra olika
    process2(argument)


main()

