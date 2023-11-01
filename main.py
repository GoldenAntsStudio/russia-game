from flask import Flask, request, render_template, session, redirect, url_for
from db import register_db, account_card, db, login_db
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'Tikhon09091'
app.permanent_session_lifetime = timedelta(days=10)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    
    if request.method == "POST":
        loginCheck = login_db(request.form['nickname'])

        if loginCheck[0] == 1 and loginCheck[1] == request.form['password']:
            user = request.form['nickname']
            session["user"] = user
            session['logged_in'] = True

            return redirect('/me')
        else:
            return render_template("login.html", error='Логин или пароль неверный')
    else:
        return render_template("login.html", error='')



@app.route("/me")
def me():
    if session.get('logged_in') == True:
        return f'<p/>{session["user"]}<p>'
    else:
        return '<p/>Вы не вошли в аккаунт!<p>'
        


    
@app.route("/work")
def work():
    if request.method == 'POST':

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        nickname_form = request.form['nickname']
        email_form = request.form['email']
        number_form = request.form['number']
        password_form = request.form['password']

        
        if register_db(nickname_form, email_form, number_form, password_form) != False:
            register_db(nickname_form, email_form, number_form, password_form)
            return '<p/>Вы успешно зарегались<p>'
        else:
            return '<p/>Никнейм или почта заняты<p>'
    else:
        return render_template("register.html")


@app.route("/<int:id>")
def account__card(id):
    
    if account_card(id):
        nickname = account_card(id)[1]
        rub = account_card(id)[2]
        usd = account_card(id)[3]
        eur = account_card(id)[4]

        return render_template('account_card.html', 
                               nickname = nickname,
                               rub = rub,
                               usd = usd,
                               eur = eur
                               )

    else:
        return '<p/>Пользователь не найден<p>'


@app.errorhandler(404)
def error(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2020)