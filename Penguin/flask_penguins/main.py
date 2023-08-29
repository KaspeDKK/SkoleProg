from flask import Flask, render_template

# Initialize application & Session
app = Flask(__name__)

@app.route('/')
def home():
    print("Website started")
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=5000)