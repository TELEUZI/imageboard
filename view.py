from app import app
from datetime import datetime
from flask import render_template, request, url_for
from funcs import get_th, create_thread
time = datetime.now().ctime()
dick = {
        'time': time,
        'status': True
    }
@app.route("/")
@app.route("/index")
def index():
    return render_template(r"index.html", name = "main")
    
@app.route("/board/<thread>", methods=['get', 'post'])
@app.route("/board", methods=['get', 'post'])
def board(thread = ""):
    th = {}
    if request.method == 'POST':
        thread_name = request.form.get('thread_name')   
        username = request.form.get('username')  # запрос к данным формы
        thread_text = request.form.get('thread_text')
        create_thread(thread_name, username, thread_text)

    print(th)
    th = get_th()["answer"]
    if (thread):
        return render_template(r"board.html", dick = th[int(thread)-1], name = thread, th = thread)
    else:
        return render_template(r"board.html", dick = th, name = "board", th = thread)
@app.route("/another_board")
def another_board():
    return render_template(r"another_board.html", dick = dick, name = "another_board")
