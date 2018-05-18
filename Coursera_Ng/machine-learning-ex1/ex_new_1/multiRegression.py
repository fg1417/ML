# The complete model to execute the whole multi-regression

import loadData
import featureNormalize
import normalEqn
import gradientDescent
import numpy

def init(number):
    return numpy.random.normal(0, 1, number + 1)

def multiRegression(number, x, y, learning_rate = 1e-3, epoch = 50):
    weights = init(number)
    for i in range(epoch):
        weights = gradientDescent.computeCost(learning_rate, weights, x, y)
    return weights

if __name__ == '__main__':
    x, y = loadData.loadData('ex1data2.txt', 2)
    x = featureNormalize.featureNormalize(x, 2)
    print normalEqn.normalEqn(x, y)
    print multiRegression(2, x, y)
