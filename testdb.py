import pymongo
import sys
from flask import *
from pymongo import MongoClient
from bson.json_util import dumps

#Flask Object

app=Flask(__name__)
s=[]
@app.route('/events',methods=['GET'])
def event():
    # connnecto to the db on standard port
    connection = MongoClient()

    # connect to the data base 
    db=connection.drone

    #collection
    a=db.createevents.find()
    
    # print all the data 
    for b in a : 
        print b
        s.append(b)    
    return dumps({'event':s})


app.run(debug=True)
