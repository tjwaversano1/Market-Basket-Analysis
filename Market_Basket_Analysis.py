import pandas as pd
import numpy as np
import matplotlib.pyplot as py

#Below are settings for the python notebook

#Gets multiple outputs in the same cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#Ignore all warnings
import warnings
warnings.filterwarnings ('ignore')
warnings.filterwarnings(action = 'ignore', category = DeprecationWarning)

#Display all rows and columns of a dataframe instead of a truncated version
from IPython.display import display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Loading Customer Dataset
CDS = pd.read_csv('')