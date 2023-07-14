#import Flask, session, redirect, render_template
from flask import Flask, render_template, request, redirect, jsonify, session, url_for
import os
import sqlite3



# Create a Flask instance
app = Flask(__name__)
app.secret_key = os.urandom(24)


#route /
@app.route('/')
#define index
def index():  # put application's code here
    #if there is a "username" in session
    if "username" in session:
        #render the template if logged in. username is the username in session
        return render_template('index.html', username=session["username"])
    else:
        #render the template if not logged in. Username is not shown
        return render_template('index.html')


# ----------------------------------------------
# ------------ A P I  R O U T E S --------------
# ----------------------------------------------


@app.route('/api/post/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #depends on what login method we are using (apple oauth or our custom login method)
        return jsonify({"status": 202})

    else:
        return jsonify({"status": 405})

@app.route('api/login', methods=['GET', 'POST'])
def login():
    #depends on what login method we are using (apple oauth or our custom login method)
    return jsonify({"status": 418})

@app.route('api/post/registercommunity', methods=['GET', 'POST'])
def registercommunity():
    if request.method == 'POST':
        print("sex")
    else:
        return jsonify({"status": 405})
    return jsonify({"status": 418})

@app.route('api/get/<userID>/info', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify({"status": 418})

@app.route('api/get/community/<communityID>/info', methods=['GET', 'POST'])
def community():
    if request.method == 'GET':
        return jsonify({"status": 418})




if __name__ == '__main__':
    app.run()




