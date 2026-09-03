# Supervised Learning Algorithms

A comprehensive repository containing implementations, theory, and usage examples of foundational Supervised Machine Learning algorithms for classification and regression tasks.

---

## 📌 Overview

Supervised Learning algorithms learn from **labeled training data** containing input features ($X$) and ground-truth targets ($y$). The primary goal is to map $f(X) \to y$ to accurately generalize predictions to unseen data.

---

## 🚀 Algorithm Directory

### 📈 Regression Algorithms (Continuous Targets)

* **Linear Regression (Simple & Multiple)**
  * Models a linear relationship between features and a continuous outcome by minimizing Mean Squared Error ($\text{MSE}$).
* **Polynomial Regression**
  * Extends linear regression by adding polynomial terms to capture non-linear feature relationships.
* **Ridge Regression ($L_2$ Regularization)**
  * Prevents overfitting and handles multicollinearity by penalizing large coefficient weights.
* **Lasso Regression ($L_1$ Regularization)**
  * Performs feature selection by driving non-essential feature coefficients to exactly zero.
* **ElasticNet Regression**
  * Combines $L_1$ and $L_2$ regularization penalties to balance feature selection and coefficient shrinkage.

### 🏷️ Classification Algorithms (Categorical Targets)

* **Logistic Regression**
  * Uses the Sigmoid function ($\sigma(z) = \frac{1}{1 + e^{-z}}$) to estimate class probabilities for binary or multi-class outputs.
* **K-Nearest Neighbors (KNN)**
  * Non-parametric algorithm that classifies a data point based on the majority vote of its $k$ closest neighbors.
* **Support Vector Machines (SVM)**
  * Finds the optimal hyper-plane that maximizes the margin separating distinct classes in feature space.
* **Naive Bayes (Gaussian, Multinomial, Bernoulli)**
  * Probabilistic classifier based on Bayes' Theorem under the strong assumption of feature independence.

### 🌲 Tree & Ensemble Methods (Regression & Classification)

* **Decision Trees (CART)**
  * Splits data into hierarchical decision nodes using metrics like Gini Impurity or Information Gain (Entropy).
* **Random Forest**
  * An ensemble of decision trees trained on bootstrapped datasets (Bagging) to reduce variance.
* **Gradient Boosting Machines (GBM / XGBoost / LightGBM)**
  * Sequential ensemble technique that builds trees iteratively to correct the errors of preceding trees.
* **AdaBoost (Adaptive Boosting)**
  * Combines weak learners by dynamically reweighting misclassified instances in subsequent iterations.

---

## 🛠️ Performance Metrics

* **Regression:** Mean Squared Error ($\text{MSE}$), Root Mean Squared Error ($\text{RMSE}$), Mean Absolute Error ($\text{MAE}$), $R^2$ Score.
* **Classification:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC.

---

## 📦 Project Structure

```text
supervised-learning/
├── linear_models/
│   ├── linear_regression.py
│   ├── ridge_lasso.py
│   └── logistic_regression.py
├── tree_models/
│   ├── decision_tree.py
│   ├── random_forest.py
│   └── xgboost_model.py
├── instance_based/
│   ├── knn.py
│   └── svm.py
├── requirements.txt
└── README.md
