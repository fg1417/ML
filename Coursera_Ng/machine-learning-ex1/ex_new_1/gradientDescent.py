# Compute the cost function
# Update weights

import numpy as np

def computeCost(learning_rate, w, x, y = None):
    bias = np.ones(len(y))
    x = np.column_stack((x, bias))
    p = np.sum(x * w, axis = 1)
    if y == None:
        return p
    else:
        delta = np.dot((p - y).transpose(), x)/len(p)
        w = w - learning_rate * delta
        # cost = 0.5*np.sum(np.dot(err.transpose(), err))/len(err)
        return w
