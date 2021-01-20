import time
from models import check_users_password, create_new_user, get_messages, set_new_messages
from flask import request


def post_data():
    data = request.json
    username = data["username"]
    text = data["text"]
    time = data["time"]
    set_new_messages(username, text, time)
    return {"database": get_messages()}


def get_data():
    massages_database = get_messages()
    return {"database": massages_database}


def checkpassword():
    data = request.json
    username = data["username"]
    password = data["password"]
    return {"answer": check_users_password(username, password)}


def passget():
    return "Everything is OK!"


def create_user():
    data = request.json
    username = data["username"]
    password = data["password"]
    return {"answer": create_new_user(username, password)}
