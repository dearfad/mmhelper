#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Medical Manuscript Helper
~~~~~~~~~~~~~~~~~~~~~~~~~
An application that can help to create medical manuscript draft fast and rationally.
:mmhelper.py: Main Program
:copyright: (c) 2018 by Dearfad
:Email: dearfad@sina.com
:license: GPL-v3
"""

import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import ShuffleSplit
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

def main():
    """Main Function."""
    dataframe = pd.read_csv('./data/duct/duct.csv')
    X = dataframe.values[:, 1:]
    y = dataframe.values[:, 0]
    # iris = load_iris()
    # X = iris.data
    # y = iris.target

    loocv = LeaveOneOut()
    sscv = ShuffleSplit()
    xgbc = XGBClassifier()
    axis_x = np.arange(1,11)
    axis_y = cross_val_score(xgbc, X, y, cv=sscv)

    print(axis_y)
    print(axis_y.mean())

    # plt.plot(axis_x, axis_y)
    # plt.show()

if __name__ == '__main__':
    main()
