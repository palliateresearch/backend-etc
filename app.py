#import Flask, session, redirect, render_template
from flask import Flask, render_template, request, redirect, jsonify, session, url_for
import os

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if "username" in session:
        return redirect('/home')
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print("recieved login request")
        if username == "nishka":
            if password == "1":
                print("logged in")
                session["username"] = username
                return redirect('/home')
        else:
            return render_template("login.html", error="Incorrect username or password")
    else:
        print("Rendering login page")
        return render_template("login.html")

@app.route('/new')
def makeaccount():
    if "username" in session:
        return redirect('/home')
    else:
        return render_template('makeaccount.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if "username" in session:
        session.pop("username", None)
        return redirect('/')
    else:
        return redirect('/')


@app.route('/home')
def home():
    if "username" in session:
        return render_template('home.html')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run()
