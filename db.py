#Импорт модулей
import sqlite3

db = sqlite3.connect("DataBase.db", check_same_thread=False)
cur = db.cursor()


def commit():
    print('COMMITING')
    db.commit()

#Проверка при ходе в аккаунт
def login_db(nickname):
    cur.execute('SELECT EXISTS (SELECT 1 FROM User WHERE nickname = ?)', (nickname,))
    existUser = cur.fetchone()[0]

    cur.execute('SELECT password FROM User WHERE nickname = ?', (nickname,))
    password = cur.fetchall()[0][0]

    return existUser, password
    
#Регистрация, запись данных нового игрока в базу данных
def register_db(nickname, email, number, password):
    
    emailBool = cur.execute('SELECT email FROM User WHERE nickname=?', (email,))
    
    accountBool = cur.execute('SELECT * FROM User WHERE nickname=?', (nickname,))

    if accountBool.fetchone() is None and emailBool.fetchone() is None:
        cur.execute('INSERT INTO User (nickname, email, number, password) VALUES(?, ?, ?, ?)', (nickname, email, number, password))
        cur.execute('INSERT INTO Property (rub, eur, usd) VALUES(?, ?, ?)', (250, 0, 0))
        commit()
    else:
        return False


#Отображение имущества и валют
def account_card(id):
    cur.execute('SELECT nickname FROM User WHERE id = ?', (id,))
    nick = cur.fetchone()
    nickname = nick[0]

    cur.execute('SELECT rub, eur, usd FROM Property WHERE id = ?', (id,))
    properties = cur.fetchall()
    rub = properties[0][0]
    usd = properties[0][1]
    eur = properties[0][2]
    if nickname:
        return id, nickname, rub, usd, eur
    else:
        return 'Пользователь не найден'
    