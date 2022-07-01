

# Write a program that plays fizz buzz up to a number the user picks.
# Fizz buzz is played by counting up from the number 1.
# If a number is divisible by 3 it's replaced by fizz.
# If it's divisible by 5 it's replaced by buzz.
# And if it's divisible by both it's replaced by fizz buzz.
# if divisible by 7 output wuzz


#######################################################################################
# Här är en extra lösning för hur man kan låta användaren genera delarna och fraserna.
# Detta görs genom att låta en dictionary ersätta den tidigare fizzword funktionen.
#######################################################################################

# tar in data från användaren
def userInput():
    argument = int(input("How far should I count? "))
    # förbereder listan och ordboken
    divisors = []
    phraseDictionary = {}
    while True:
        divisor = int(input("Which divisor should be added? Use -1 to finish adding phrases. "))
        if divisor == -1:
            break
        phrase = input("And which phrase? ")
        # Lägger till delarna till listan och uppslaget till ordboken.
        divisors.append(divisor)
        phraseDictionary.update({divisor: phrase})
    return argument, divisors, phraseDictionary


# går igenom alla delarna och avgör om någon delar talet num
def isDivisble(num, divisors):
    for divisor in divisors:
        if num % divisor == 0:
            return True
    return False


# avgör vilken sträng som ska skrivas ut och skriver ut denna
def process(endpoint, divisors, phraseDictionary):
    for x in range(1, endpoint + 1):
        result = ""
        # avancerad for loop som utför nedanstående för alla tal i listan
        for divisor in divisors:
            # om x är delbart med den givna delaren så bifogas den associerade frasen
            if x % divisor == 0:
                result = result + phraseDictionary.get(divisor)
        # om x är delbart med någon av delarna skriver vi ut frasen
        if isDivisble(x, divisors):
            print(result)
        # annars skrivs talet ut
        else:
            print(x)


# kallar på userInput() och använder resultatet som argument till process()
def main():
    argument, divisors, phraseDictionary = userInput()
    process(argument, divisors, phraseDictionary)


main()
