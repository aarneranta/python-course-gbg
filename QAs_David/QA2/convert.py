# Write a program to convert fahrenheit to celcius
# 0 degrees celcius is 32 degrees fahrenheit
# 100 degrees celcius is 212 degrees fahrenheit


def f2c(fahrenheit):
    return 9/5 * (fahrenheit - 32)


def c2f(celcius):
    return 5/9 * celcius + 32


def main():
    choice = input("Vill du konvertera från fahrenheit, skriv f, eller från celcuis skriv c")
    if choice == "f":
        fahrenheit = float(input("Skriv in tempen i fahrenheit: "))
        celcius = f2c(fahrenheit)
        print("Tempen i celcius är", celcius)
    elif choice == "c":
        celcius = float(input("Skriv in tempen i celcius: "))
        fahrenheit = c2f(celcius)
        print("Tempen i fahrenheit är", fahrenheit)
    else:
        print("Vad håller du på med?")


main()
