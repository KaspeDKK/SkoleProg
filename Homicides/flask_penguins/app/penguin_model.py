from flask import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pickle


#loaded_penguin_model = pickle.load(open('flask_penguins\static\models\penguin_model' , 'rb'))

def test_model():
    """
    # Read the CSV file
    penguins = pd.read_csv("flask_penguins/static/data/penguins.csv")
    penguins_original = pd.read_csv("flask_penguins/static/data/penguins.csv")
    
    # Select columns with float64 data type
    penguins = penguins.select_dtypes(include='float64')
    
    # Remove specific columns & Empty Rows
    columns_to_remove = ["Delta 15 N (o/oo)", "Delta 13 C (o/oo)"]
    penguins = penguins.drop(columns=columns_to_remove)
    penguins = penguins.dropna()
    
    # Include the "Species" column from the original sheet
    species_column = penguins_original['Species']
    penguins = pd.concat([penguins, species_column], axis=1)
    d = {'Adelie Penguin (Pygoscelis adeliae)': 0, 'Chinstrap penguin (Pygoscelis antarctica)': 1, 'Gentoo penguin (Pygoscelis papua)': 2}
    penguins['Species'] = penguins['Species'].map(d)
    features = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)']
    X = penguins[features]
    y = penguins['Species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test


    y_pred = loaded_penguin_model.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return accuracy
    """

def id_penguin():
    """
    int_features = [int(x) for z in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = loaded_penguin_model.predict(final_features)    
    return 'name_of_penguin'
    """

