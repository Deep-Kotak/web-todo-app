from flask import Flask
from database import create_table

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    return "<h1>Web To-Do List App</h1>"

if __name__ == "__main__":
    app.run(debug=True)