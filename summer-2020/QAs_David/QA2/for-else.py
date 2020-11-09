favouriteFruit = "orange"

for fruit in ["apple", "banana", "lemon"]:
    print(fruit)
    if fruit == favouriteFruit:
        print("Found my favourite fruit")
        # Break avslutar for-loopen 
        # Detta för att det är onödigt att fortsätta iterera när vi 
        # hittat det vi vill
        break

# Else-klausulen exekveras endast då for-loopen genomfördes utan 
# att påträffa ett break, dvs om vi inte hittade vad vi sökte
else:
    print("My fruit is not here :(")
