from strategy import Strategy
from strategy_type import StrategyType
import numpy as np


months = ['gener', 'febrer', 'març', 'abril', 'maig', 'juny', 'juliol', 'agost', 'setembre', 'octubre', 'novembre', 'desembre']
all_temps = np.loadtxt('bcn_temps.csv')
#all_temps = all_temps[200:len(all_temps)]
years = all_temps[:,0]

Strategy.build_run(StrategyType.LINEAR, months, years, all_temps)
Strategy.build_run(StrategyType.POLYNOMIAL, months, years, all_temps)
#Strategy.build_run(StrategyType.RIDGE, months, years, all_temps)
#Strategy.build_run(StrategyType.LASSO, months, years, all_temps)
