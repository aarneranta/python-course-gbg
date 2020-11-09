# - - - List comprehension - - - 

# Väldigt ofta vill man ta en lista och göra något med alla element i listan
# Så som vi lärt oss hittils skulle detta se ut som

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newValues = []
for value in values:
    newValues.append(value * 2)


# Python erbjuder dock något som heter list comprehension,
# med detta blir ovanstående kod
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newValues = [value**2 for value in values]


# När man skapar en lista med list comprehension kan man även filtrera listan
# genom att sätta en if-sats i slutet
values = [-3, -2, -1, 0, 1, 2, 3]
newValues = [1/value for value in values if value != 0]


# - - - Lambdas - - -

# Ni har sett att funktioner i python är precis som andra variable
# Man kan binda dem till namn

def square(x):
    return x**2

newNameForSameFunction = square

print(newNameForSameFunction(2) == 4)  # True

# Och man kan skicka dem som argument till andra funktioner

def doTwice(f, x):
    return f(f(x))

print(doTwice(square, 2))  # 16 ty det är (2^2)^2

# Om vi vill skicka en mycket enkel funktion till en annan funktion är
# det omständigt att skriva def functionName(arg1, arg2): osv
# Istället kan vi använda lambda

# lambda x: x**2 är en funktion som tar ett argument 
# och returnerar det till höger om :

print(doTwice(lambda x: x**2, 2))  # 16
print(doTwice(lambda x: x * 5, 2))  # 50












# Om vi sätter samman dessa (jag vet dock inte varför vi någonsin skulle vilja
# göra detta, men python gör det möjligt :) får vi detta
# listOfFunctions = [(lambda x: x**n) for n in range(3) if n % 2 == 0]
listOfFunctions = [(lambda x: x**n) for n in range(3)]
# En lista med funktioner som upphöjer en siffra till jämna tal.
# Låt oss använda denna för att hitta jämna potenser av 2
print([f(2) for f in listOfFunctions])
# Funkar inte???
