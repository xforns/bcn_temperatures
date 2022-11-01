from regression_linear import RegressionLinear
from regression_poly import RegressionPoly
from regression_ridge import RegressionRidge
from regression_lasso import RegressionLasso
from strategy_type import StrategyType

class Strategy:

    @staticmethod
    def build_run(type, months, years, all_temps):
        obj = None
        if type == StrategyType.LINEAR:
            obj = RegressionLinear(type)
        elif type == StrategyType.POLYNOMIAL:
            obj = RegressionPoly(type)
        elif type == StrategyType.RIDGE:
            obj = RegressionRidge(type)
        elif type == StrategyType.LASSO:
            obj = RegressionLasso(type)
        if obj == None:
            return

        res = obj.calculate(months, years, all_temps)
        if res is None:
            return
        obj.plot(res, months, years, all_temps)
