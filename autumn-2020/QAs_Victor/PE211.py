# Uppgift 2.11 med hjälp av 2.9 och ~2.10

# 2.11:
# Write a program that performs any unit conversion of your choosing.
# Make sure that it prints an introduction that explains what it does.

# Börja med att bygga upp progeramstrukturen, top down!

# Metoder för att göra konversionenerna
# Tänk på descriptiva variabelnamn
def mtofeet(meters):
    return meters * 3.2808399

def feettom(feet):
    return feet * 0.3048

def ctof(degrees):
    return degrees*1.8 + 32

def ftoc(degrees):
    return (degrees-32)/1.8

# Kontroller för in och output
def main():
    print('Hallå eller?!','Vad vill du konvertera mellan?\n',
            'meter till fot (1),', 'fot till meter (2),\n',
            'celcius till farenhight (3),', 'farenhight till celcius (4)')
    # Farligt men han körde den på föreläsnignen
    selection,value = eval(input('(metod,värde): '))
    # Kan göra såhär istället men list comprehention kommer senare
    #selection,value = [int(val) for val in input('(metod,värde): ').split(',')]
    if selection == 1:
        output = mtofeet(value)
        print('Enkelt:', output, 'fot')
    elif selection == 2:
        output = feettom(value)
        print('Enkelt:', output, 'm')
    elif selection == 3:
        output = ctof(value)
        print('Enkelt:', output, 'f')
    elif selection == 4:
        output = ftoc(value)
        print('Enkelt:', output, 'c')
    else:
        print('Ange ett av de listade alternativen!')
        print('------------------------------------')
        main()
        # Skulle kunna separera ut inputen eller wrappa i en loop för att göra
        # det snyggare

main()
