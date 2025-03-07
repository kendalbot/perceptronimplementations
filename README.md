# perceptronimplementations
Tired of treating machine learning like a black box. I can paste code snippets, tweak hyper parameters, and get results but struggling to explain "under the hood" better. Minimalistic perceptron implementations. Not to replace optimized libraries but to prove to myself that I understand what is happening and why



"The perceptron is the most basic form of a neural network developed by Frank Rosenblatt in 1957, essentially a simpliefied model of a biological neuron. It is a binary classifier that maps a input vector "x" to an output value using a simple computation
output = 1 if (w·x + b > 0) else 0
Where:

w is a vector of weights
x is the input vector
b is the bias term
w·x is the dot product

The perceptron learns by adjusting weights when it makes mistakes
If it predicts 0 when it should predict 1, increase weights for active inputs
If it predicts 1 when it should predict 0, decrease weights for active inputs
The algorithm converges to a solution for any linearly separable problem.
