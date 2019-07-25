import matplotlib.pyplot as plt
import numpy as np


def convert_kwargs(kwargs):
    
    for mpl_key, tft_key in zip(('s', 'c'), ('size', 'color')):
        try:
            val = kwargs.pop(tft_key)
        except KeyError:
            continue
        else:    
            kwargs[mpl_key] = val
            
    return kwargs

def _scatter(plot, x, y, **kwargs):
    
    kwargs = convert_kwargs(kwargs)
    plot.ax.scatter(x, y, **kwargs)

def handle_colors(plot, x, y, **kwargs):
    # Note/TODO: This could be faster by setting the color as an array instead
    # of doing the groupby operation. Consider refactoring if it's really slow.
    color = kwargs.pop('color')
    series =  plot.data[color]
    if series.dtype == np.dtype("O"):
        ## Colors from categorical column
        for group, group_data in plot.data.groupby(color):
            _scatter(plot, group_data[x], group_data[y], label=group, **kwargs)
        
    else:
        ## Colors from numerical column
        _scatter(plot, plot.data[x], plot.data[y], color=plot.data[color], **kwargs)
    plot.labels(x, y)

def handle_df(plot, x, y, **kwargs):
        
        color = kwargs.get('color', None)
        if color in plot.data.columns:
            handle_colors(plot, x, y, **kwargs)
        else:
            _scatter(plot, plot.data[x], plot.data[y], **kwargs)
            plot.labels(x, y)
        return plot

class ScatterMixin:
    """ Mixin class for Plot class that implements the scatter plot. 
        Attributes available from Plot class include:
          - data: a DataFrame, possibly None
          - ax: Matplotlib axis object
    """
            
    def scatter(self, x=None, y=None, size=None, color=None, **kwargs):
        if self.data is not None:
            handle_df(self, x, y, size=size, color=color, **kwargs)
        else:
            _scatter(self, x, y, size=size, color=color, **kwargs)
        return self