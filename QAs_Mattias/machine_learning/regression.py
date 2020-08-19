from numpy import array, polyfit, linspace, mean, square, power
from numpy.random import random, seed
from matplotlib import pyplot as plt


def create_noisy_data(x_data, r):
    seed(2)
    return array([x + r * random(1) - r/2 for x in x_data])


def polynomial(c, x):
    x = array([x]).T
    return sum([c[i] * power(x, i) for i in range(len(c))])


lower, upper, points, r = 1, 15, 15, 6

x_data = linspace(lower, upper, points)
data = create_noisy_data(x_data, r)

# We now demonstrate different degrees of polynomials, to see the error in the fitted curves in relation to the points
# However, higher degree polynomials generalise much worse to our linear data, so don't be deceived by the MSE!
# Remember to view the image in full screen
plt.figure(1)
for i in range(1, 16):
    coefficient = polyfit(x_data, data, deg=i)[::-1]
    fitted_data = polynomial(coefficient, x_data)
    mse = mean(square(fitted_data - data))

    # To get a higher resolution for the polynomial
    x_data_fit = linspace(lower, upper, points * 4)
    fitted_data = polynomial(coefficient, x_data_fit)

    # At higher, we will get a warning. This is due to overfitting!
    plt.subplot(3, 5, i)
    plt.plot(x_data, data, 'rx', label='Original data')
    plt.plot(x_data_fit, fitted_data, label='Fitted data')
    plt.title("Degree: {}".format(i) + ", MSE: {:.2f}".format(mse))
    plt.legend(loc=0)
    plt.grid()

plt.show()