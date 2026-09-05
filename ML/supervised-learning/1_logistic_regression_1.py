"""
FinanceDevelop a logistic regression example that will predict 
whether a loan applicant will Default ($y=1$) or Not Default($y=0$)
based on two input features: Debt-to-Income ratio ($x_1$) and Credit Score ($x_2$)."""

import numpy as np
from sklearn.linear_model import LogisticRegression

#create data sets
#Traing set
X_train = np.array([
    [0.45, 580],[0.20, 750],[0.55, 610],[0.15, 800],
    [0.38, 640],[0.25, 710],[0.50, 590],[0.30, 690],
    [0.60, 520],[0.18, 780],[0.42, 630],[0.28, 700]
])
y_train = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

#Test set
X_test = np.array([
    [0.48, 600],[0.22, 740],
    [0.52, 570],[0.19, 770]
])
y_test = np.array([1, 0, 1, 0])

#create object of LogisticRegression model 
model = LogisticRegression()

#train model
model.fit(X_train,y_train)

#prediction 
prediction = model.predict(X_test)
print(f"prediction : {prediction}")
