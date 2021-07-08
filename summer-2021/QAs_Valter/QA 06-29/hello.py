
# Uppgift: skriv ett program som tar input och ger output, konverterar fahrenheit till celsius.
# Formel: Celsius = subtrahera 32 från fahrenheit och multiplicera med 5/9.

def fahr_to_celsius(x):
    return (x - 32) * 5/9


for fahr in range(0, 101, 10):
    celsius = fahr_to_celsius(fahr)
    print(fahr, "fahrenheit motsvarar", celsius, "celsius.")
