from threads.models import create_new_thread, get_threads, create_new_post
from flask import request


# def post_data():
#     data = request.json
#     username = data["username"]
#     text = data["text"]
#     time = data["time"]
#     set_new_messages(username, text, time)
#     return {"database": get_messages()}


# def get_data():
#     massages_database = get_messages()
#     return {"database": massages_database}


# def checkpassword():
#     data = request.json
#     username = data["username"]
#     password = data["password"]
#     return {"answer": check_users_password(username, password)}


# def passget():
#     return "Everything is OK!"


def create_thread(thread_name, username, thread_text):
    print("111")
    return {"answer": create_new_thread(thread_name, username, thread_text)}
    
def get_th(threads):
    return {"answer": get_threads(threads)}

def create_post(thread, username, thread_text):
    return {"answer": create_new_post(thread, username, thread_text)}