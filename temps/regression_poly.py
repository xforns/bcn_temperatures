from regression_strategy import RegressionStrategy
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import matplotlib as mpl
import matplotlib.pyplot as plt

class RegressionPoly(RegressionStrategy):

    def calculate(self, months, years, all_temps):
        poly = PolynomialFeatures(degree=4, include_bias=False)
        poly_features = poly.fit_transform(years.reshape(-1, 1))
        poly_reg_model = LinearRegression()

        res = []
        for idx in range(len(months)):
            temps = all_temps[:,idx+1]
            poly_reg_model.fit(poly_features, temps)
            res.append(poly_reg_model.predict(poly_features))
        return res

    def plot_fun(self, res, idx, years):
        return res[idx]
