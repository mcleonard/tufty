import matplotlib.pyplot as plt
import numpy as np


def _line(ax, x, y, **kwargs):
    ax.plot(x, y, **kwargs)

def handle_df(plot, x, y, color=None):
    y_data = plot.data[y]
    if x == 'index':
        x_data = plot.data.index
    else:
        x_data = plot.data[x]
    
    _line(plot.ax, x_data, y_data, color=color)

class LineMixin:
    def line(self, x, y, color=None):
        if self.data is not None:
            handle_df(self, x, y, color=color)

        else:
            _line(self.ax, x, y, color=color)
        
        return self