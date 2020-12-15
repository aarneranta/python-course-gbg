def getNumeric(prompt):
    while True:
        try:
            res = float(input(prompt))
            break
        except ValueError:
            print("Numbers only please!")
        except (KeyboardInterrupt, EOFError):
            return None
    return res


def main():
    s = 0
    while True:
        i = getNumeric("Enter next number to add to sum: ")
        if i:
            s += i
        else:
            print()
            break
    print(f"The sum is {s}")


if __name__ == "__main__":
    main()
