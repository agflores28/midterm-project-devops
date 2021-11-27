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

@app.route('/login', methods = ["GET", "POST"])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    else:
        user_name = request.form['user_name']
        password = request.form['password']
        rec = tuple(user_collection.find({'$and':[{'user_name': user_name, 'password': password}]}).limit(1) )
        if rec:
            return render_template('welcome.html',Registered = True, user_name = rec[0]['user_name'])

        else:
            return render_template('login.html', Invalid = True)


@app.route('/signup', methods = ["GET", "POST"])
def signup():

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        user_name = request.form['user_name']
        password = request.form['password']
        new_user = {
        "first_name": first_name,
        "last_name": last_name,
        "user_name": user_name,
        "password": password
        }
        if tuple(user_collection.find({'user_name': user_name}).limit(1)):
            return render_template('signup.html', Existing = True)

        else:
            user_collection.insert_one(new_user)
            return render_template('signup.html',Success = True, user_name = user_name)

    else:
        return render_template('signup.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2828)