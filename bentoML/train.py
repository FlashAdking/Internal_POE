
import pandas as pd 
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
import bentoml

raw = load_iris()

print(raw.feature_names)

X = raw.data
y = raw.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = svm.SVC(kernel='rbf', C=1)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")


save_svc = bentoml.sklearn.save_model("svc_iris_model", model)

print(f"Model saved with BentoML: {save_svc}")