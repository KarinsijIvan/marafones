import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect('back/login_and_password.db')
        return con
    except sqlite3.Error:
        print("Error")


def sql_insert(con, entities):
    cursor = con.cursor()
    cursor.execute('INSERT INTO employees(login, password) VALUES(?, ?)', entities)
    con.commit()

con = sql_connection()
entities = ('Alex777cool', '123')
sql_insert(con, entities)