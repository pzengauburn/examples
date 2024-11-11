######################################################################
# Examples for logistic regression
# Peng Zeng (Auburn University)
# updated: 11-10-2024
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
# fit logistic regression using statmodels 
######################################################################

import statsmodels.api as sm 

x_aug = sm.add_constant(x)

model1 = sm.Logit(y, x_aug)
result = model1.fit() 
result.summary()

result.aic              # AIC
result.bic              # BIC 
result.params           # fitted coefficients 
result.bse              # SE of coefficients 
result.pvalues          # test the significance of variables 
result.conf_int()       # 95% CI for coefficients 
result.predict()        # fitted probabilities 
result.cov_params()     # variance of parameters 

######################################################################
# fit logistic regression using statmodels with l1-penalty 
######################################################################

resultx = model1.fit_regularized(method = 'l1', alpha = 0.1)
resultx.summary()

######################################################################
# fit logistic regression using GLM
######################################################################

model2 = sm.GLM(y, x_aug, family = sm.families.Binomial())
result2 = model2.fit()
result2.summary()

result2x = model2.fit_regularized(method = 'elastic_net', alpha = 0.01, L1_wt = 0.0)
result2x.params

######################################################################
# fit logistic regression using sklearn 
######################################################################

from sklearn.linear_model import LogisticRegression 

model3 = LogisticRegression(penalty = None)
model3.fit(x, y)
model3.intercept_       # fitted intercept
model3.coef_            # fitted coefficients 

model3.predict_proba(x)[:, 1]

######################################################################
# fit logistic regression using sklearn with l1 or l2 or others 
######################################################################

model4 = LogisticRegression(penalty = 'l2', C = 2, solver = 'saga')
model4.fit(x, y)
model4.intercept_ 
model4.coef_ 

######################################################################
# compute AUC 
######################################################################

from sklearn.metrics import roc_auc_score 

y_probs = result.predict() 
auc = roc_auc_score(y, y_probs)
print(f"AUC = {auc:.4f}")

######################################################################
# draw ROC curve
######################################################################

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve 

fpr, tpr, thresholds = roc_curve(y, y_probs) 

plt.figure()
plt.plot(fpr, tpr, label = f"AUC = {auc:.2f}")
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line for a random classifier
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic (ROC) Curve")
plt.legend(loc = "lower right")
plt.show()

######################################################################
# THE END
######################################################################
