"""
nn.py

This code demonstrates a single neuron, several of which might
make up a more complex neural network.
Loosely based on an introduction to neural networks by Andrew Task.

A neuron essentially consists of two parts.
 1) The linear combination of inputs with their respective weights,
    e.g. this neuron with three inputs calculates
    w_1 * x_1 + w_2 * x_2 + w_3 * x_3
    (which we in linear algebra call a dot product between vectors w and x)
 2) An activation function evaluated with the result of the above linear
    combination.

It is very common to work on the range [0,1], and therefore commonly we choose
activation functions that have results on this range.
Here we use a so-called sigmoid function (do you recognize it from QA1?)
which elegantly forces us to stay in that range.
Also, it has a very convenient expression for the derivative.
If we know the value V of the function at some point x the derivative at
that point is V(1-V).

To train our neuron we also need some form of backpropagation,
or feedback, to make it "learn" the correct weights given some training data.
This is where the derivate becomes useful, as we can adjust weights based
on the loss (here deviation from expected output) scaled with the derivative
so that the altered input to the function becomes closer to the expected output
(without going into too much mathematical detail).

This very simple example trains the neuron on
0 0 1 | 0
1 1 1 | 1
1 0 1 | 1
0 1 1 | 0
and tries to predict the result of [1 0 0].
An astute human will probably notice that the first input correlates perfectly
with the output, and so will guess that the result should be 1.
What happens with the neuron? What kind of weights can we expect?
"""

import numpy as np

training_set_inputs = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
training_set_outputs = np.array([[0, 1, 1, 0]]).T

def sigmoid(x):
    return 1/(1 + np.exp(-x))

np.random.seed(1234)
weights = 2 * np.random.random((3,1)) - 1
for i in range(1000):
    output = sigmoid(np.dot(training_set_inputs, weights))
    weights += np.dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))

print(sigmoid(np.dot(np.array([1,0,0]), weights)))
print(weights)
