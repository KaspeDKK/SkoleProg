from flask import *
from app.star_model import *

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

# Initialize application & Session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'HTX123'  

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test_model_penguin/', methods=['POST'])
def test_model_penguin():
    accuracy_result = test_model()
    return render_template('home.html', accuracy_result=accuracy_result)

@app.route('/identify/')
def identify():
    if request.method == "POST":
        print(request.form)

        arr = []
        for i in request.form.items():
            arr.append(i[1])

        print(arr)
        prediction = star_model.predict(np.array(arr).reshape(1, -1))[0]
    return render_template('identify.html', pred=prediction)

@app.route('/identify_penguin/', methods=['POST'])
def identify_penguin():
    penguin_result = id_penguin()
    return render_template('identify.html', penguin_result=penguin_result)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=5000)