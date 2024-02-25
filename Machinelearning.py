import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

url = "https://github.com/JonathanC13/ML-Iris-dataset/blob/master/dataset/iris.csv"

# Plot multivariate plots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
data.plot(kind='scatter', x='sepal-length', y='sepal-width', ax=axs[0, 0])
data.plot(kind='scatter', x='sepal-width', y='petal-length', ax=axs[0, 1])
data.plot(kind='scatter', x='sepal-width', y='petal-width', ax=axs[1, 0])
data.plot(kind='hist', x='target', ax=axs[1, 1])
plt.tight_layout()
plt.show()

# Plot univariate plots
data.plot(kind='hist', x='petal-width')
data.plot(kind='hist', x='petal-length')
data.plot(kind='hist', x='sepal-width')
data.plot(kind='hist', x='sepal-length')
plt.show()

# Prepare the dataset for machine learning
X = data.drop('target', axis=1)
y = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Implement the six machine learning algorithms
models = [
    ('Logistic Regression', LogisticRegression()),
    ('Decision Tree Classifier', DecisionTreeClassifier(max_depth=3)),
    ('K Neighbors Classifier', KNeighborsClassifier(n_neighbors=3)),
    ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
    ('Gaussian Naive Bayes', GaussianNB()),
    ('Support Vector Classifier', SVC(kernel='linear', C=1))
]

# Train and evaluate the models
for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'{name} accuracy: {accuracy}')

# Find the algorithm with the highest accuracy
max_accuracy = max(accuracy for name, model in models for accuracy in [accuracy_score(y_test, model.predict(X_test))])
best_model = [(name, model) for name, model in models if accuracy_score(y_test, model.predict(X_test)) == max_accuracy]
print(f'The algorithm with the highest accuracy is {best_model[0][0]} with an accuracy of {max_accuracy}')
