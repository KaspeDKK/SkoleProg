from flask import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pickle

"""
    int_features = [int(x) for z in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = loaded_penguin_model.predict(final_features)    
    
    return 'name_of_penguin'
"""

def load_model():
    model = pickle.load(open('flask_penguins\static\models\penguin_model' , 'rb'))
    return model

def test_model():
    """
    # Read the CSV file
    stars = pd.read_csv("data/Stars.csv")
    stars_original = pd.read_csv("data/Stars.csv")


    y_pred = model.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return accuracy
    """

