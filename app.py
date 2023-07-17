#import Flask, session, redirect, render_template
from sqlalchemy import create_engine, Column, String, Integer, BigInteger, JSON, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, jsonify, session, url_for
import uuid
import os
import sqlite3
import bcrypt

db = SQLAlchemy()

def generateRandomID():
    randomID = uuid.uuid4()
    return str(randomID)


# Create a Flask instance
app = Flask(__name__)
app.secret_key = os.urandom(24)


#Database stuff
engine = create_engine('mysql+pymysql://sql9632805:Tq1nniKxiS@sql9.freemysqlhosting.net:3306/sql9632805')
#Base = declarative_base(bind=engine)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class CommunityDatabase(Base):
    __tablename__ = 'community'
    ParkID = Column(String(40), primary_key=True)
    ParkName = Column(String(255))
    LifetimeWattageGeneration = Column(BigInteger)
    TimezoneCode = Column(String(3))
    DailyWattageGeneration = Column(JSON)
    RegisteredUsers = Column(JSON)
    CBadgesComplete = Column(JSON)
    CBadgesInProgress = Column(JSON)
    CBadgesDone = Column(JSON)

class UserDatabase(Base):
    __tablename__ = 'user'
    UserID = Column(String(40), primary_key=True)
    Username = Column(String(255))
    ActualName = Column(String(255))
    LifetimeWattageGeneration = Column(BigInteger)
    DailyWattageGeneration = Column(JSON)  
    IsParent = Column(Boolean)
    ChildrenList = Column(JSON)  
    ParkID = Column(String(40))
    Password = Column(String(255))
    BadgesComplete = Column(JSON)  
    BadgesInProgress = Column(JSON)  
    BadgesDone = Column(JSON)  

    def __init__(self, **kwargs) -> None:
        super(UserDatabase, self).__init__(**kwargs)
        self.id = generateRandomID()
       
        db.session.add(self)
        db.session.commit()

    # CBadge = Community Badge
    # Badge = User Badge

# Create the table if it doesn't exist
metadata = MetaData()
Base.metadata.create_all(bind=engine)


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
        requestBody = request.get_json()
    try:
        username = requestBody.get("username")
        actualname = requestBody.get("actualname")
        password = requestBody.get("password")
        isParent = requestBody.get("isParent")
        childrenList =  requestBody.get("childrenList")
    except:
        return "Invalid JSON arguments", 400
    existingUser = user.query.filter_by(username = username).first()
    if existingUser is not None:
        return "Username already exists", 400
    encodedPassword = str(password).encode("utf-8")
    hashedPassword = bcrypt.hashpw(password=encodedPassword, salt=bcrypt.gensalt())
    hashedPassword = hashedPassword.decode("utf-8")
    user = UserDatabase(Username=username, ActualName = actualname, IsParent = isParent, ChildrenList = childrenList, hashedPassword=hashedPassword)
    return jsonify(user.id)

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    #depends on what login method we are using (apple oauth or our custom login method)
    return jsonify({"status": 418})

@app.route('/api/post/registercommunity', methods=['GET', 'POST'])
def registercommunity():
    if request.method == 'POST':
        print("")
    else:
        return jsonify({"status": 405})
    return jsonify({"status": 418})

@app.route('/api/get/<userID>/info', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify({"status": 418})

@app.route('/api/get/community/<communityID>/info', methods=['GET', 'POST'])
def community():
    if request.method == 'GET':
        return jsonify({"status": 418})




if __name__ == '__main__':
    app.run()


session.commit()
session.close()
