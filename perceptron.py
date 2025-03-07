import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        
    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        
        for _ in range(self.epochs):
            for idx, x_i in enumerate(X):
                y_pred = 1 if np.dot(x_i, self.weights) + self.bias > 0 else 0
                update = self.lr * (y[idx] - y_pred)
                self.weights += update * x_i
                self.bias += update
                
    def predict(self, X):
        return [1 if np.dot(x_i, self.weights) + self.bias > 0 else 0 for x_i in X]

#Example #&AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])
model = Perceptron()
model.fit(X, y)
print(model.predict(X))