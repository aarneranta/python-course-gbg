# Write a function that returns the sum of the first n integers
# Write a function that returns the sum of the cube of the first n integers


# Can't be called sum as this interfers with builtin
def sum_(values):
    s = 0
    for value in values:
        s += value

    return s


def sumMap(values, f):
    s = sum_([f(value) for value in values])
    return s


def main():
    values = range(1, 100)
    print(f"sum of first 100 integers: {sum_(values)}")
    print(f"Sum of first 100 cubes: {sumMap(values, lambda x: x**3)}")
    values = [value for value in range(1, 10000) if "9" in str(value)]
    print(f"sum of first reciprocal: {sumMap(values, lambda x: 1/x)}")
    print(f"sum of first reciprocal squares: {sumMap(values, lambda x: 1/x**2)}")


main()
