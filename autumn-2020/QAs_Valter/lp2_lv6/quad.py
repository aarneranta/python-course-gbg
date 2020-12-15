""" Allows user to enter coefficients to a second degree polynomial (ax^2+bx+c) and computes the roots. """


def quad(a, b, c):
    disc = b**2 - 4 * a * c
    if disc < 0:
        return None
    elif abs(disc) < 0.01:
        return -b / (2 * a)
    else:
        x1 = (-b + disc**(1 / 2)) / (2 * a)
        x2 = (-b - disc**(1 / 2)) / (2 * a)
        return x1, x2


def main():
    input_str = input("Enter three coefficients in the form a,b,c: ")
    try:
        x, y, z = map(lambda x: x.strip(), input_str.split(','))
        a, b, c = map(lambda x: int(x), (x, y, z))
    except ValueError as e:
        print("Please enter three numbers in the form a,b,c!")
        main()
    except Exception as e:
        print(f"Unknown error: {e}")
    roots = quad(a, b, c)
    if roots is None:
        print("Imaginary roots!")
    else:
        print(roots)


if __name__ == "__main__":
    main()
