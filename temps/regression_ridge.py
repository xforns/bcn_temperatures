from regression_strategy import RegressionStrategy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from numpy.random import default_rng

class RegressionRidge(RegressionStrategy):

    def calculate(self, months, years, all_temps):
        years = years.reshape(-1, 1)
        rng = default_rng()
        all_temps_rs = all_temps.reshape(-1,1)
        noisy_temps = all_temps_rs + 0.5 * rng.standard_normal(len(all_temps_rs))
        ridge = Ridge(alpha = 0.5)
        res = []
        ridge.fit(all_temps_rs, noisy_temps)
        for idx in range(len(months)):
            temps = all_temps[:,idx+1].reshape(-1, 1)
            res.append(ridge.predict(temps))
        return res

    def plot_fun(self, res, idx, years):
        return res[idx]
