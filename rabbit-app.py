from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('welcome.html')

@app.route('/about')
def more():
    return render_template('more.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2828)