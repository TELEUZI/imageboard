from flask import request

from server import app
import funcs
import time


@app.route("/")
def status():
    dick = {
        'time': time.ctime(),
        'status': True
    }
    return dick


@app.route("/view")
def view():
    return funcs.get_data()


@app.route("/send", methods=['POST'])
def send():
    return funcs.post_data()


@app.route("/checkpass", methods=['POST'])
def checkpass():
    return funcs.checkpassword()


@app.route("/reg_user", methods=['POST'])
def create_user():
    return funcs.create_user()
