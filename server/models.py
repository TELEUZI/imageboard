import pickle
import sqlite3
from sqlite3 import Error

DATABASE_PATH = "users_database.db"


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_new_user(username, password):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM users WHERE (name) = (?)", (username,))
    if data.fetchone():
        return False, "Пользователь с таким именем уже зарегистрирован!"
    cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (username, password))
    connection.commit()
    return True, "Info is correct"


def check_users_password(username, password):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM users WHERE (name,password) = (?, ?)", (username, password,))
    if data.fetchone():
        return True
    else:
        return False


def set_new_messages(username, text, time):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO messages (name, text, time) VALUES (?, ?, ?)", (username, text, time))
    connection.commit()


def get_messages():
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    data = cursor.execute("SELECT name, time, text FROM messages")
    connection.commit()
    return data.fetchall()

# con = create_connection(DATABASE_PATH)

# connection = create_connection(DATABASE_PATH)
# cursor = connection.cursor()
# data = cursor.execute("SELECT name, password FROM users ORDER BY id DESC LIMIT 10")
# print(data.fetchall())
# input()

# query = '''CREATE TABLE IF NOT EXISTS messages (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   text TEXT,
#   time TEXT NOT NULL);'''
# query = "DROP TABLE messages"
# execute_query(con, query)
# user_1 = "INSERT INTO users (name, password) VALUES ('admin','admin')"
# execute_query(con, user_1)
# user_2 = "INSERT INTO users (name, password) VALUES ('use1r','use1r')"
# execute_query(con, user_2)
# cur = con.cursor()
# data = cur.execute("SELECT * FROM users WHERE name=?", ("admin",))
# print(data.fetchone())
