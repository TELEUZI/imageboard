from app import app
from datetime import datetime
from flask import render_template, request, url_for
from threads.board import board

time = datetime.now().ctime()
dick = {
        'time': time,
        'status': True
    }
@app.route("/")
@app.route("/index")
def index():
    return render_template(r"index.html", name = "main")

app.register_blueprint(board)

@app.route("/another_board")
def another_board():
    return render_template(r"another_board.html", dick = dick, name = "another_board")
