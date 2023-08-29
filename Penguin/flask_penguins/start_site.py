from flask import Flask, render_template, redirect, session, flash
from app.config import Config
from route import web, api

from flask import Flask, render_template, redirect, session
from flask_session import Session

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import create_session
from app.dbhelper import Users, Questionaire, Questions, Answer_Log, engine
from app.forms import LoginForm, NewUserForm, QuestionaireSubmission

# Initialize application & Session
app = Flask(__name__)
app.config.from_object(Config)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(web, url_prefix="/")
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')
 

@app.route("/login/", methods=["POST", "GET"])
def login():
    loginform = LoginForm()
    
    if loginform.validate_on_submit():
        user_session = create_session(autocommit=False, autoflush=False, bind=engine)
        user = user_session.query(Users).filter_by(username=loginform.username.data).first()
        
        if user:
            if check_password_hash(user.password, loginform.password.data):
                user_session.close()
                session["name"] = loginform.username.data
                return redirect('/')
            else:
                flash("Forkert password!")
    
    return render_template('login.html', form = loginform)


@app.route("/logout/")
def logout():
    session["name"] = None
    return redirect("/")

@app.route('/new_user/', methods=['POST', 'GET'])
def new_user():
    form = NewUserForm()
    print(form.username)
    user_session = create_session(autocommit=False, autoflush=False, bind=engine)
    
    if form.validate_on_submit():
        print("validated")
        user = user_session.query(Users).filter_by(username=form.username.data).first()

        if user:
            return redirect('/login/')

        new_user = Users(username = form.username.data, password=generate_password_hash(form.password.data, method='sha256'))
        user_session.add(new_user)
        user_session.commit()

        if new_user:
            user_session.close()
            return redirect('/login/')

    else:
        print("No vallidation")
    
    return render_template('new_user.html', form=form)

@app.route("/questionaires/")
def question_menu():
    # Get all the questionaires from the database.
    questionaire_session = create_session(autocommit=False, autoflush=False, bind=engine)
    questionaires = questionaire_session.query(Questionaire.questionaire_id, Questionaire.name).all()
    print(questionaires)
        # questionaires.append(str(q).replace(')','').replace('(','').replace(',','').replace("'",'')  ) # patch solution. DUMB sqlalchemy
    #print(questionaires)

    return render_template('questionaire.html', questionaires=questionaires)

@app.route("/open_questionaire/")
def open_questionaire():
    return render_template('open_questionaire.html')

@app.route("/qurestionare/<qid>", methods=['POST', 'GET'])
def view(qid):

    form = QuestionaireSubmission()
    questionaire_session = create_session(autocommit=False, autoflush=False, bind=engine)
    questionaire_questions = questionaire_session.query(Questions.question).filter_by(q_id=qid).all()
    print(questionaire_questions)
    
    questionaire = str(questionaire_session.query(Questionaire.name).filter_by(questionaire_id=qid).all()).replace(')','').replace('(','').replace("'",'').replace('[','').replace(']','').replace(',','')


    if form.validate_on_submit():
        print("Button pressed")
        print(QuestionaireSubmission.answers)
        
        new_answer = Answer_Log(answer = QuestionaireSubmission.answers, q_id = qid, user=session["name"])
        print(new_answer)
        questionaire_session.add(new_answer)
        questionaire_session.commit()
    else: 
        print("NO VALIDATION")
    return render_template('open_questionaire.html', qid=qid, questionaire=questionaire, questionaire_questions=questionaire_questions, form=form)


if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) # Only works on LOCALHOST development servers.
    app.run(host='0.0.0.0', port=5000)