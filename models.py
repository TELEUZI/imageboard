import pickle
import sqlite3
from sqlite3 import Error
from datetime import datetime

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



def create_new_thread(thread_name, username, thread_text):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM threads WHERE (thread_name) = (?)", (thread_name,))
    if data.fetchone():
        return False, "Пользователь с таким именем уже зарегистрирован!"
    cursor.execute("INSERT INTO threads (thread_name, username, thread_text, time) VALUES (?, ?, ?, ?)", (thread_name, username, thread_text, datetime.now().ctime()))
    connection.commit()
    return True

def get_threads():
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    data = cursor.execute("SELECT thread_number, thread_name, username, thread_text, time FROM threads")
    connection.commit()
    return data.fetchall()





# con = create_connection(DATABASE_PATH)

# query = '''CREATE TABLE IF NOT EXISTS threads (
#   thread_number INTEGER PRIMARY KEY AUTOINCREMENT,
#   thread_name TEXT NOT NULL,
#   username TEXT DEFAULT Аноним,
#   thread_text TEXT,
#   time TEXT NOT NULL);'''
# execute_query(con, query)



# connection = create_connection(DATABASE_PATH)
# cursor = connection.cursor()
# data = cursor.execute("SELECT name, password FROM users ORDER BY id DESC LIMIT 10")
# print(data.fetchall())
# input()

# query = "DROP TABLE messages"

# user_1 = "INSERT INTO users (name, password) VALUES ('admin','admin')"
# execute_query(con, user_1)
# user_2 = "INSERT INTO users (name, password) VALUES ('use1r','use1r')"
# execute_query(con, user_2)
# cur = con.cursor()
# data = cur.execute("SELECT * FROM users WHERE name=?", ("admin",))
# print(data.fetchone())
