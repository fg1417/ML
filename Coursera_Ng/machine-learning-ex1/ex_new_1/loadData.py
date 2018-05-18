# Load data from txt files
# Transfer into matrices

import numpy

def loadData(datafile, number):
    data = numpy.loadtxt(datafile, delimiter = ',')
    x = []
    y = []
    for ele in data:
        x.append(ele[:number])
        y.append(ele[number])
    return x, y


if __name__ == '__main__':
    x, y = loadData('ex1data2.txt', 2)
    print len(x[0])
    print y
