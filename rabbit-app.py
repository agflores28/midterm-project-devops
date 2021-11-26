from flask import Flask
from flask import request
from flask import render_template
from flask_pymongo import pymongo


app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://agflores:219219@cluster0.xrbao.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("usersDB")
user_collection = db.records


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

@app.route('/signup', methods = ["GET", "POST"])
def signup():

    if request.methods == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        user_name = request.form['user']
        password = request.form['pass']
        new_user = {
        "fname": first_name,
        "lname": last_name,
        "user": user_name,
        "pass": password
    }
        if first_name == '' or last_name == '' or user_name == '' or password == '':
            print("Invalid!")

        else:
            user_collection.inser_one(new_user)
            print("Inserted!")

    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2828)