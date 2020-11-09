import math
# Skriv en funktion som beräknar kvadratroten av ett tal

def sqrt(x):
    # Vi vet att sqrt(x) = x / sqrt(x)
    # om vår gissning är för låg är VL för lågt och HL för högt
    # om vår gissninging är för hög är VL för hög och HL för låg
    # Då vet vi att oavsett är det rätta värdet mellan VL och HL
    # Tag nästa gissning som medelvärdet av de två

    tolerance = 1e-5

    guess = 1
    error = 1

    while error > tolerance:
        newGuess = (guess + x / guess)/2
        error = abs(newGuess - guess) * 2
        guess = newGuess
        print(guess)

    return guess

def main():
    x = float(input("Gimme a number and I'll calculate its sqrt: "))
    sqrtX = sqrt(x)
    print(f"Approx value: {sqrtX}\nActual value: {math.sqrt(x)}")


main()

