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
    th_time = datetime.now().ctime()
    cursor.execute("INSERT INTO pipeline (time) VALUES (?)", (th_time,))
    
    th_unique = cursor.execute("SELECT thread_number FROM pipeline WHERE (time) = (?)", (th_time,)).fetchone()
    
    cursor.execute("INSERT INTO threads (thread_number, thread_name, username, thread_text, time) VALUES (?, ?, ?, ?, ?)", (th_unique[0], thread_name, username, thread_text, th_time))
    query = '''CREATE TABLE IF NOT EXISTS t_{} (
  thread_number INTEGER,
  username TEXT DEFAULT Аноним,
  thread_text TEXT,
  time TEXT NOT NULL);'''.format(th_unique[0])
    execute_query(connection, query)
    cursor.execute(f"INSERT INTO t_{th_unique[0]} (thread_number, username, thread_text, time) VALUES (?, ?, ?, ?)", (th_unique[0], username, thread_text, th_time))
    connection.commit()
    connection.close()
    return True
def create_new_post(thread, username, thread_text):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    th_time = datetime.now().ctime()
    cursor.execute("INSERT INTO pipeline (time) VALUES (?)", (th_time,))
    th_unique = cursor.execute("SELECT thread_number FROM pipeline WHERE (time) = (?)", (th_time,)).fetchone()
    cursor.execute(f"INSERT INTO t_{thread} (thread_number, username, thread_text, time) VALUES (?, ?, ?, ?)", (th_unique[0], username, thread_text, th_time))
    connection.commit()
    connection.close()

def get_threads(table):
    connection = create_connection(DATABASE_PATH)
    cursor = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS t_{} (
  thread_number INTEGER,
  username TEXT DEFAULT Аноним,
  thread_text TEXT,
  time TEXT NOT NULL);'''.format(table)
    execute_query(connection, query)
    if (table == "threads"):
        data = cursor.execute("SELECT thread_number, thread_name, username, thread_text, time FROM {}".format(table))
    else:
        data = cursor.execute("SELECT thread_number, username, thread_text, time FROM t_{}".format(table)) 
    return data.fetchall()


# connection = create_connection(DATABASE_PATH)
# query = '''CREATE TABLE IF NOT EXISTS pipeline (
#   thread_number INTEGER PRIMARY KEY AUTOINCREMENT,
#   time TEXT NOT NULL);'''
# execute_query(connection, query)
# connection = create_connection(DATABASE_PATH)
# cursor = connection.cursor()
# th_time = datetime.now().ctime()
# cursor.execute("INSERT INTO pipeline (time) VALUES (?)", (th_time,))
# connection.commit()