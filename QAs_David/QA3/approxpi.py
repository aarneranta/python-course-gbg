import math
# Write a function that approximates pi with n terms in the series
# pi = 4/1 - 4/3 + 4/5 - 4/7 + ...


def piproximator2000(n):
    piprox = 0
    for i in range(n):
        term = (-1)**i * 4 / (2 * i + 1)
        piprox += term

    return piprox


def main():
    print(f"Final value:  {piproximator2000(100)}\nActual value: {math.pi}")


main()
