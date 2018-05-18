# Normalize the data using mean and std.

import pickle
import numpy

def normalize(data, number):
    f = open('normalize.txt', 'rb')
    factor = pickle.load(f)
    data = numpy.mat(data)
    for i in range(0, number):
        data[:, i] = data[:, i] - factor['mean'][i]
        data[:, i] = data[:, i]/factor['std'][i]
    return numpy.array(data)

def featureNormalize(data, number):
    data_mean = numpy.mean(data, axis = 0)
    data_std = numpy.std(data, axis = 0)
    factor = {'mean': data_mean, 'std': data_std}
    f = open('normalize.txt', 'wb')
    pickle.dump(factor, f)
    f.close()

    return normalize(data, number)
