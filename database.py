import sqlite3 as sql

def connectdb():
    conn = sql.connect('users.db')
    c = conn.cursor()
    qry = "SELECT firstname, lastname FROM app_users"
    c.execute(qry)
    userlist = c.fetchall()
    return userlist


def pushtodb(username, firstname, lastname, password):
    try:
       conn = sql.connect('users.db')
       c = conn.cursor()
    except Error as e:
        print(e)
    userinfo = (username, firstname, lastname)
    pwinfo = (username, password)
    c.execute("INSERT INTO app_users VALUES(?,?,?)", userinfo)
    c.execute("INSERT INTO user_pws VALUES(?, ?)", pwinfo)
    conn.commit()


def checkcreddb(username, password):
    try:
       conn = sql.connect('users.db')
       c = conn.cursor()
    except Error as e:
        print(e)
    c.execute("SELECT password FROM user_pws WHERE username = (?)", (username,))
    passworddb = c.fetchone()
    if passworddb is not None:
        passworddb = passworddb[0]
        if password == passworddb:
            return 1
    else:
        return 0


def deletefromdb(username):
    try:
       conn = sql.connect('users.db')
       c = conn.cursor()
    except Error as e:
        print(e)
    c.execute("DELETE * FROM app_users WHERE username = (?)", (username,))
    c.execute("DELETE * FROM user_pws WHERE username = (?)", (username,))
    conn.commit()

def checkartist(artist):
    try:
       conn = sql.connect('contemporaryartists.db')
       c = conn.cursor()
    except Error as e:
        print(e)

