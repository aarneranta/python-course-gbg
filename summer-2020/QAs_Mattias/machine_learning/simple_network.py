from numpy import array, random, dot, zeros, mean, square
from matplotlib import pyplot as plt
from time import time


class NeuralNetwork:
    def __init__(self, iterations):
        random.seed(1)
        # We model a network consisting of 2 inputs and 1 output and assign random weights.
        self.weights = 2 * random.random((2, 1)) - 1
        self.iterations = iterations
        self.history = zeros(iterations)
        self.bias = 2 * random.random() - 1

    # train changes self.weights to better solve the problem.
    # This is the real Machine Learning-part!
    def train(self, inputs, outputs, learning_rate):
        for iteration in range(self.iterations):
            prediction = self.predict(inputs)
            error = outputs - prediction
            adjustment = learning_rate * dot(inputs.T, error)
            self.weights += adjustment
            self.history[iteration] = square(mean(error))

    def predict(self, inputs):
        return dot(inputs, self.weights)

    def get_history(self):
        return self.history


iterations = 1000
learning_rate = 0.01
neural_network = NeuralNetwork(iterations)

# The training set
inputs = array([[2, 3], [1, 1], [5, 2], [12, 3]])
outputs = array([[10, 4, 14, 30]]).T
# The formula is the sum of the numbers, times 2.

# Training the neural network using the training set.
start_time = time()
neural_network.train(inputs, outputs, learning_rate)

end_time = time()
training_time = end_time - start_time
print("Elapsed time for training:", training_time)

# Try out the neural network!
condition = True
while condition:
    try:
        test_input = input("Write two numbers separated by comma (x, y) to test out the network: ")
        if test_input.lower() == "exit":
            condition = False
        else:
            test_input = test_input.split(', ')
            test_input = array([int(element) for element in test_input])
            print("Model prediction: ", neural_network.predict(test_input))
            print("Actual value from formula:", 2 * (test_input[0] + test_input[1]))

    except ValueError:
        print("Incorrect format. Default input is [15, 2]")
        default_input = array([15, 2])
        print("Model prediction: ", neural_network.predict(default_input))
        print("Actual value from formula:", 2 * (default_input[0] + default_input[1]))
        condition = False

plt.plot(neural_network.get_history()[0:100])
plt.xlabel("Iteration")
plt.ylabel("Mean squared error (MSE)")
plt.title("Learning curve: MSE per iteration")
plt.grid()
plt.show()