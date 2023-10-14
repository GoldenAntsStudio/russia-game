from flask import Flask, request, render_template, session
from db import register_db, account_card

app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    



    return render_template("login.html")

@app.route("/log", methods=['POST', 'GET'])
def log():
    nickname_form = request.form['nickname']
    password_form = request.form['password']

    session.new
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/reg", methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':

        nickname_form = request.form['nickname']
        email_form = request.form['email']
        number_form = request.form['number']
        password_form = request.form['password']

        
        if register_db(nickname_form, email_form, number_form, password_form) != 'НИК ЗАНЯТ':
            register_db(nickname_form, email_form, number_form, password_form)
            return '<p/>Вы успешно зарегались<p>'
        else:
            return '<p/>Ник занят<p>'

        
    else:
        print("ERROR")

@app.route("/<int:id>")
def account__card(id):
    
    if account_card(id):
        return render_template('account_card.html', nickname = account_card(id))
    else:
        return '<p/>Пользователь не найден<p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')