import matplotlib.pyplot as plt
import numpy as np

def main():
    print("Detta är ett program som illustrerar kaos")

    rs = np.linspace(0, 4, 200)

    n = 400

    for r in rs:
        x = 0.5
        xs = []
        for i in range(n):
            x = r * x * (1 - x)
            xs.append(x)

        plt.plot([r]*200, xs[n-200:], '.', markersize=1)

    # For loopen slut
    plt.show()


main()
