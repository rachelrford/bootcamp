#Compilation of functions built during the bootcamp

import numpy as np
import matplotlib as plt

def ecdf(data):
    """
    Compute the empirical cumulative distribution function of a set of data
    """
    #Order the data from smallest to largest number
    x = np.sort(data)
    #Set normalized even spacing in y according to index
    y = np.arange(1, len(data) + 1) / len(data)
    return x, y
