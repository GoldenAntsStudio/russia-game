import sqlite3
#USER DB
user_db = sqlite3.connect("user.db", check_same_thread=False)
user_cur = user_db.cursor()
#PROPERTY DB
property_db = sqlite3.connect("property.db", check_same_thread=False)
property_cur = property_db.cursor()

def commit():
    print('COMMITING')
    user_db.commit()


def register_db(nickname, email, number, password):
    accountBool = user_cur.execute('SELECT * FROM User WHERE nickname=?', (nickname,))
    if accountBool.fetchone() is None:
        user_cur.execute('INSERT INTO User (nickname, email, number, password) VALUES(?, ?, ?, ?)', (nickname, email, number, password))
        commit()
    else:
        return "НИК ЗАНЯТ"


def account_card(id):
    user_cur.execute('SELECT nickname FROM User WHERE id = ?', (id,))
    nick = user_cur.fetchone()
    nickname = nick[0]
    if nickname:
        return nickname
    else:
        return 'Пользователь не найден'
    