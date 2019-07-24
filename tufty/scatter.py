import matplotlib.pyplot as plt
import numpy as np

class ScatterMixin:
            
    def scatter(self, x=None, y=None, size=None, color=None):
        if color in self.data.columns:
            series =  self.data[color]
            if series.dtype == np.dtype("O"):
                for group, group_data in self.data.groupby(color):
                    self.ax.scatter(group_data[x], group_data[y], s=size, label=group)
                    self.ax.set_xlabel(x)
                    self.ax.set_ylabel(y)
            else:
                self.ax.scatter(self.data[x], self.data[y], s=size, c=self.data[color])

        else:
            self.ax.scatter(self.data[x], self.data[y], s=size, c=color)
            self.ax.set_xlabel(x)
            self.ax.set_ylabel(y)
        return self