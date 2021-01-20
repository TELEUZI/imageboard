from flask import Flask
import views
app = Flask(__name__)
app.secret_key = "hell"

if __name__ == "__main__":
    app.run(debug=True)