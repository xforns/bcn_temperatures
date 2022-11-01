from regression_strategy import RegressionStrategy
import numpy as np
from scipy import stats

class RegressionLinear(RegressionStrategy):

    def calculate(self, months, years, all_temps):
        res = []
        for idx in range(len(months)):
            temps = all_temps[:,idx+1]
            res.append(stats.linregress(years, temps))
        return res

    def plot_fun(self, res, idx, years):
        return res[idx].intercept + res[idx].slope * years
