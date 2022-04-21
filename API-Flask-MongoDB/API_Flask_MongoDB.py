#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# API_Flask_MongoDB.py
#######################

import os

from flask import Flask,render_template,request,url_for,redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost',27017)

db = client.flask_db

todos = db.todos

@app.route('/',methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.route('/delete/<id>/',methods=["POST"])
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':

    homeDir = os.environ['HOME']
    userID = homeDir.split("/")[-1]

    if userID[2] == "6":
        port = "2" + userID[3:7]
    if userID[2] == "7":
        port = "3" + userID[3:7]

    print("Personal API Port: %s" %(port))

    app.run(port=int(port),host='0.0.0.0',use_reloader=True)
