from flask import *
from app.penguin_model import test_model

# Initialize application & Session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'HTX123'  

@app.route('/')
def home():
    print("Website started")
    return render_template('home.html')

@app.route('/test_model_penguin/', methods=['POST'])
def test_model_penguin():
    accuracy_result = test_model()
    return render_template('home.html', accuracy_result=accuracy_result)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=5000)