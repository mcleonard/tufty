import matplotlib.pyplot as plt
from . scatter import ScatterMixin
from . line import LineMixin

class Plot(ScatterMixin, LineMixin):
    def __init__(self, data=None, ax=None, title=None):
        self.data = data
        if ax is None:
            self.fig, self.ax = plt.subplots()
        else:
            self.fig = ax.figure
            self.ax = ax

        self.ax.set_title(title)

    def legend(self, *args, **kwargs):
        self.ax.legend(*args, **kwargs)
        return self

    def title(self, text, **kwargs):
        self.ax.set_title(text, **kwargs)
        return self

    def labels(self, x=None, y=None, **kwargs):
        if x:
            self.ax.set_xlabel(x, **kwargs)
        if y:
            self.ax.set_ylabel(y, **kwargs)
        return self

    def __repr__(self):
        return "tufty.Plot"

def subplots(data=None, figsize=None, nrows=1, ncols=1, w_pad=1, h_pad=1):
    """ 
    Arguments
    ---------

    data: either one DataFrame or a list of DataFrames
    """
    fig, axes = plt.subplots(figsize=figsize, nrows=nrows, ncols=ncols)
    fig.tight_layout(w_pad=w_pad, h_pad=h_pad)

    if len(data) <= len(axes.flatten()):
        return [Plot(df, ax=ax) for df, ax in  zip(data, axes.flatten())]
    else:
        return [Plot(data, ax=ax) for ax in axes]
