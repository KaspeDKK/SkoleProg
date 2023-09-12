from flask import *


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
    return render_template('identify.html')

@app.route('/identify_penguin/', methods=['POST'])
def identify_penguin():
    penguin_result = id_penguin()
    return render_template('identify.html', penguin_result=penguin_result)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Kører kun på localhost
    app.run(host='0.0.0.0', port=5000)