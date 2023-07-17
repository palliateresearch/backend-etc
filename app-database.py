#import Flask, session, redirect, render_template
from flask import Flask, render_template, request, redirect, jsonify, session, url_for
from . import db
import os
import uuid
from sqlalchemy import create_engine, Column, String, Integer, BigInteger, JSON, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
#Base.metadata.create_all()
metadata = MetaData()
Base.metadata.create_all(bind=engine)

# Generate a random UUID for ParkID
# how 2 add uuid:  park_id = str(uuid.uuid4())

# Example data
#park_name = "Example Park"
#lifetime_wattage_generation = 1000000
#timezone_code = "PST"
#daily_wattage_generation = [30, 40, 35, 23, 34]  # Example values
#registered_users = []  # Example values
# Create a new Community instance
#community = Community(
#    ParkID=park_id,
#    ParkName=park_name,
#    LifetimeWattageGeneration=lifetime_wattage_generation,
#    TimezoneCode=timezone_code,
#    DailyWattageGeneration=daily_wattage_generation,
#    RegisteredUsers=registered_users
#)
# Add the instance to the session and commit changes
#session.add(community)
session.commit()
session.close()










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


