from flask import Flask, render_template, redirect, session, flash

# Initialize application & Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) # Only works on LOCALHOST development servers.
    app.run(host='0.0.0.0', port=5000)