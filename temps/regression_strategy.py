import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as style

class RegressionStrategy:

    def __init__(self, type):
        self.type = type
        print("Building for type: " + self.type.name)
        style.use('seaborn-dark')

    def calculate(self, months, years, all_temps):
        pass


    def subplot(self, idx, res, months, years, all_temps):
        fig, axs = plt.subplots(int(len(months)/4), 2)
        plt.xlim([years[0], years[len(years)-1]])
        axs_row = 0
        axs_col = 0
        for i in range(int(len(months)/2)):
            temps = all_temps[:,idx+1]
            axs[axs_col, axs_row].plot(years, temps)
            plot_fun = self.plot_fun(res, idx, years)
            axs[axs_col, axs_row].plot(years, plot_fun)
            axs[axs_col, axs_row].set_title(months[idx])
            if axs_col == int(len(months)/4)-1:
                axs_col = 0
                axs_row = 1
            else:
                axs_col = axs_col + 1
            idx = idx + 1

        fig.suptitle(self.type.name)
        plt.show()

    def plot(self, res, months, years, all_temps):
        self.subplot(0, res, months, years, all_temps)
        self.subplot(int(len(months)/2), res, months, years, all_temps)

    def plot_fun(self, res, idx, years):
        pass
