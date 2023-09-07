from flask import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pickle


loaded_star_model = pickle.load(open('flask_star\static\models\star_model' , 'rb'))

def test_model():

    # Read the CSV file
    stars = pd.read_csv("data/Stars.csv")
    stars_original = pd.read_csv("data/Stars.csv")

    d = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    stars['Type'] = stars['Type'].map(d)

    # Merge similar color names
    stars['Color'] = stars['Color'].str.lower()  # Convert to lowercase to ensure consistency
    stars['Color'] = stars['Color'].replace({
        'blue white': 'blue-white',
        'yellow-white': 'white-yellow',
        'yellowish white': 'yellowish'
    })

    # Encode the colors
    color = {
        'red': 0, 
        'blue-white': 1, 
        'white': 2, 
        'blue': 3, 
        'yellowish': 4, 
        'pale yellow orange': 5, 
        'whitish': 6, 
        'white-yellow': 7, 
        'orange': 8, 
        'orange-red': 9
    }
    stars['Color'] = stars['Color'].map(color)

    # Define the encoding dictionary for Spectral_Class
    spectral_class = {
        'O': 0,
        'B': 1,
        'A': 2,
        'F': 3,
        'G': 4,
        'K': 5,
        'M': 6
    }

    # Encode the Spectral_Class column
    stars['Spectral_Class'] = stars['Spectral_Class'].map(spectral_class)
    
    # Include the "Species" column from the original sheet
    species_column = star_original['Species']
    star = pd.concat([star, species_column], axis=1)
    d = {'Adelie star (Pygoscelis adeliae)': 0, 'Chinstrap star (Pygoscelis antarctica)': 1, 'Gentoo star (Pygoscelis papua)': 2}
    star['Species'] = star['Species'].map(d)
    features = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)']
    X = star[features]
    y = star['Species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test


    y_pred = loaded_star_model.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return accuracy

def id_star():
    """
    int_features = [int(x) for z in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = loaded_star_model.predict(final_features)    
    return 'name_of_star'
    """

