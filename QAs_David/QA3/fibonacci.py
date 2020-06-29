# Write a funciton that takes n as an argument and returns the
# nth fibonacci number
# 1, 1, 2, 3, 5, 8, 13, 

def fibonacci(n):
    if n==1 or n==2:
        return 1

    f_k, f_k_1 = 1, 1
    for _ in range(n-2):
        f_k, f_k_1 = (f_k + f_k_1), f_k
        # FEL
        # f_k = f_k + f_k_1
        # f_k_1 = f_k

    return f_k


# Use this function to approximate the golden ratio

# f_k = f_k_1 * phi
# phi = f_k / f_k_1

# phi^2 * x = x + phi * x

# (1 + sqrt(5)) / 2

def approxGoldenRatio(n):
    for i in range(1, n):
        phi = fibonacci(i+1) / fibonacci(i)
        print(phi)

    return phi


def main():
    print(f"Approx value: {approxGoldenRatio(10)}\nActual value: {(1 + 5**0.5)/2}")


main()

