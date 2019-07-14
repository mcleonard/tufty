
import matplotlib.pyplot as plt

# Defining styles here
DEFAULT = {'axes.facecolor': '#e5e5e5',
           'axes.edgecolor': "white",
           'axes.grid': True,
           'grid.color': "white",
           'grid.linewidth': 1.5,
           'axes.axisbelow': True,
           'xtick.bottom': False,
           'ytick.left': False,
           'font.size': 13,
           'font.sans-serif': ['Open Source Sans',
                               'Helvetica Neue',
                               'Helvetica', 
                               'DejaVu Sans',
                               'Bitstream Vera Sans',
                               'Computer Modern Sans Serif',
                               'Lucida Grande',
                               'Verdana',
                               'Geneva',
                               'Lucid',
                               'Arial',],
           'axes.labelsize': 15,
           'axes.titlesize': 16,
           'legend.edgecolor': 'white',
           'legend.facecolor': 'white',
           'legend.fancybox': False,
           'legend.fontsize': 14,
           'legend.framealpha': 0.7,
           'legend.frameon': True}

styles = {'default': DEFAULT}

def style(name=None, style_dict=None):
    if style_dict:
        style_dict = style_dict
    elif name is None:
        style_dict = styles['default']
    else:
        style_dict = styles['name'] 
    plt.rcParams.update(style_dict)