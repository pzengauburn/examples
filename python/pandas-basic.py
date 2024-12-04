######################################################################
# Examples for pandas  
# Peng Zeng (Auburn University)
# updated: 2024-12-04
######################################################################

import pandas as pd 

filelink = "http://www.auburn.edu/~zengpen/teaching/STAT-7030/datasets/neuralgia.txt"
neuralgia = pd.read_csv(filelink, delim_whitespace = True)

neuralgia.info()                       # display a concise summary

neuralgia.describe()                   # summary statistics for numeric variables 
neuralgia.describe(include = 'all')    # summary statistics for all variables 

######################################################################
# add new columns 
######################################################################

neuralgia[['A', 'B']] = 0 
neuralgia['new'] = [item + '_Pain' for item in neuralgia['Pain']]
neuralgia = neuralgia.assign(C = neuralgia['Age'] + neuralgia['Duration'])

######################################################################
# THE END
######################################################################
