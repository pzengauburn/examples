######################################################################
# Examples for creating dummy variables 
# Peng Zeng (Auburn University)
# updated: 2024-12-03
######################################################################

import pandas as pd 

df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue', 'Green'],
                   'Value': [2, 1, 3, 5, 0, 4]})

######################################################################
# use pandas.get_dummies()  
######################################################################

# detect categorical variables, and create dummy variables
dummy = pd.get_dummies(df) 

# drop one dummy variable for each categorical variable to avoid multicollinearity 
dummy1 = pd.get_dummies(df, drop_first = True) 

# handle selected variables, and customize names 
dummy2 = pd.get_dummies(df['Color'], prefix = 'x')

######################################################################
# use OneHotEncoder()   
######################################################################

from sklearn.preprocessing import OneHotEncoder 

encoder = OneHotEncoder(sparse_output = False)
df_encoded = encoder.fit_transform(df[['Color']])  
feature_names = encoder.get_feature_names_out(['Color'])

dummies = pd.DataFrame(df_encoded, columns = feature_names)
df_new = pd.concat([df, dummies], axis = 1)

# you can drop the original variable Color if you do not needed it 
df_new.drop('Color', axis = 1, inplace = True)

# handle unknown categories with handle_unknown = 'ignore' in OneHotEncoder() 

# when using pd.concat(), we can ignore the index with ignore_index = True 

######################################################################
# THE END
######################################################################
