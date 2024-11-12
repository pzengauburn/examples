######################################################################
# Examples for xgboost
# Peng Zeng (Auburn University)
# updated: 11-12-2024
######################################################################

import pandas as pd 

filelink = "http://www.auburn.edu/~zengpen/teaching/STAT-7030/datasets/neuralgia.txt"
neuralgia = pd.read_csv(filelink, delim_whitespace = True)
neuralgia.info()
neuralgia.describe(include = 'all')

neuralgia.Pain.value_counts()
y = neuralgia.Pain.map({"Yes": 1, "No": 0})
x = pd.get_dummies(neuralgia[["Treatment", "Sex", "Age", "Duration"]],
                   drop_first = True)

######################################################################
# XGBoost
######################################################################

import xgboost as xgb
dtrain = xgb.DMatrix(x, label = y)

# set parameters for binary classification 
params = {
    "objective": "binary:logistic",
    "eval_metric": "logloss"
}
model = xgb.train(params, dtrain)

# compute predicted probabilities 
dtest = xgb.DMatrix(x)
pred_prob = model.predict(dtest)

# compute AUC 
from sklearn.metrics import roc_auc_score 

auc = roc_auc_score(y, pred_prob)
print(f"AUC = {auc:.4f}")

######################################################################
# THE END
######################################################################
