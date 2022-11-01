from regression_strategy import RegressionStrategy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from numpy.random import default_rng

class RegressionLasso(RegressionStrategy):

    def prep_training_data(self, months, years, all_temps):
        print(all_temps.shape)

    def calculate(self, months, years, all_temps):
        self.prep_training_data(months, years, all_temps)

        res = None
        return res

    def plot_fun(self, res, idx, years):
        return res[idx]
