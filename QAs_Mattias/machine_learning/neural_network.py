from numpy import array, random, dot, zeros, mean, square, sum
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
        nr_inputs = inputs.shape[0]
        for iteration in range(self.iterations):
            prediction = self.predict(inputs)
            error = (outputs - prediction) / nr_inputs

            # Weights & biases are added with derivatives in MSE with respect to themselves, times a learning rate.
            # "dot" multiplies corresponding weights with inputs and adds, so (w1 * x1) + (w2 * x2) + ...
            # ".T" transposes a matrix/vector.
            self.weights += learning_rate * dot(inputs.T, error)
            self.bias += learning_rate * sum(error)
            # Save the loss history. Loss is for us, mean squared error.
            self.history[iteration] = square(mean(error))

    def predict(self, inputs):
        # We do not use any activation functions here. Simply weighting the inputs with learned weights will do.
        # What we get here is (w1 * x1 + w2 * x2) + b
        return dot(inputs, self.weights) + self.bias

    def get_history(self):
        return self.history


def training_data(n):
    # randint((10, 10)): two numbers 0-9
    return array([random.randint((10, 10)) for i in range(n)])


def formula(inputs):
    return 2 * array([[sum(element) for element in inputs]]).T - 1


iterations = 10000
learning_rate = 0.01
neural_network = NeuralNetwork(iterations)

# The training set
inputs = training_data(10)
outputs = formula(inputs)
# The formula is the sum of the numbers, times 2, minus 1.

# Training the neural using the training set.
start_time = time()
neural_network.train(inputs, outputs, learning_rate)

end_time = time()
training_time = end_time - start_time
print("Elapsed time for training:", training_time)
print("Learned weights: {}".format(neural_network.weights.T))
print("Learned bias: {}".format(neural_network.bias))

# Try out the neural network!
condition = True
while condition:
    try:
        test_input = input("Write two numbers separated by comma (x, y) to test out the neural network: ")
        if test_input.lower() == "exit":
            condition = False
        else:
            test_input = test_input.split(', ')
            test_input = array([[int(element) for element in test_input]])
            print("Model prediction: ", neural_network.predict(test_input))
            print("Actual value from formula: ", formula(test_input))

    except ValueError:
        default_input = array([[15, 2]])
        print("Incorrect format. Default input is {}".format(default_input))
        print("Model prediction: ", neural_network.predict(default_input))
        print("Actual value from formula: ", formula(default_input))
        condition = False

plt.plot(neural_network.get_history()[0:100])
plt.xlabel("Iteration")
plt.ylabel("Mean squared error (MSE)")
plt.title("Learning curve: MSE per iteration")
plt.grid()
plt.show()
