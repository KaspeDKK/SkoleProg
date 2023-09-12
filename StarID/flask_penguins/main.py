from flask import *
from app.star_model import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pickle

# Initialize application & Session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'HTX123'  

model = pickle.load(open('StarID\star_model' , 'rb'))

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/id/', methods=["GET", "POST"])
def id():
    if request.method == "POST":
        print(request.form)

        arr = []
        for key, value in request.form.items():
            if key == "Color":
                # Encode the colors
                value = value.lower()  # Convert to lowercase to ensure consistency
                color_map = {
                    'blue white': 'blue-white',
                    'yellow-white': 'white-yellow',
                    'yellowish white': 'yellowish'
                }
                value = color_map.get(value, value)  # Replace if key exists, else use original value

                color_encoding = {
                    'red': 0, 
                    'blue-white': 1, 
                    'white': 2, 
                    'blue': 3, 
                    'yellowish': 4, 
                    'pale-yellow-orange': 5, 
                    'whitish': 6, 
                    'white-yellow': 7, 
                    'orange': 8, 
                    'orange-red': 9
                }
                value = color_encoding[value]
            elif key == "Sclass":
                spectral_class_encoding = {
                    'O': 0,
                    'B': 1,
                    'A': 2,
                    'F': 3,
                    'G': 4,
                    'K': 5,
                    'M': 6
                }
                value = spectral_class_encoding[value]
            elif key == "id_star_button":
                continue  # Skip this value, since its the button
            else:
                # Convert numerical strings to float
                value = float(value)

            arr.append(value)

        print(arr)
        prediction = model.predict(np.array(arr).reshape(1, -1))[0]
    return render_template('home.html', prediction=prediction)


@app.route('/test_model_penguin/', methods=['POST'])
def test_model_penguin():
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Kører kun på localhost
    app.run(host='0.0.0.0', port=5000)