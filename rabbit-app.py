from flask import Flask
from flask import request
from flask import render_template
from flask.pymongo import pymongo


app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://agflores:219219@cluster0.xrbao.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


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

@app.route('/signup', methods = ["POST"])
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2828)