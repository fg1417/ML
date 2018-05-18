# The complete model to execute the whole multi-regression

import loadData
import featureNormalize

x, y = loadData.loadData('ex1data2.txt', 2)
featureNormalize.featureNormalize(x, 2)
