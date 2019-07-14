import urllib
import pandas as pd

def iris():
    url = "https://raw.githubusercontent.com/mcleonard/tufty-data/master/iris.csv"
    response = urllib.request.urlopen(url)
    return pd.read_csv(response)