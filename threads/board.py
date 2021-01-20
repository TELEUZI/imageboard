from flask import Blueprint
from flask import render_template, request
from datetime import datetime
from threads.funcs import get_th, create_thread, create_post
import re
re1 = lambda z : re.findall(r'>>\d+', z)
board = Blueprint('board', __name__, static_folder='static', template_folder='templates', url_prefix='/board')
time = datetime.now().ctime()


@board.route('/', methods = ['post', 'get'])
def index():
    if request.method == 'POST':
        thread_name = request.form.get('thread_name')   
        username = request.form.get('username')  # запрос к данным формы
        thread_text = request.form.get('thread_text')
        create_thread(thread_name, username, thread_text)
    dick = get_th("threads")
    return render_template('threads/board.html', dick = dick['answer'], get_th = get_th)

@board.route('/<thread>', methods = ['post', 'get'])
def thread(thread):
    
    if request.method == 'POST':   
        username = request.form.get('username')  # запрос к данным формы
        thread_text = request.form.get('thread_text')
        create_post(int(thread), username, thread_text)
    dick = get_th(thread)
    return render_template('threads/thread.html', dick = dick['answer'])