'''1 . Write a program to insert a record in sql table via api
2.  Write a program to update a record via api
3 . Write a program to delete a record via api
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well'''

import mysql.connector as connection
from flask import Flask,request,jsonify

app=Flask(__name__)

mydb=connection.connect(host="localhost",user="root",passwd="Asdfghjkl$1")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb" )
cursor.execute("create table if not exists taskdb.mysqltable(name varchar(30),number int)")

@app.route('/insert',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.mysqltable values(%s, %s)",(name,number))
        mydb.commit()
        return jsonify(str("successfully inserted"))

@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        cursor.execute("update taskdb.mysqltable set number=number+500 where name = %s",(get_name,))
        mydb.commit()
        return(jsonify(str("updated successfully")))

@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        name_delete=request.json['name_delete']
        cursor.execute("delete from taskdb.mysqltable where name=%s",(name_delete,))
        mydb.commit()
        return(jsonify(str("deleted successfully")))

@app.route('/fetch',methods=['POST'])
def fetch_data():
    cursor.execute("select * from taskdb.mysqltable")
    l=[]
    for i in cursor.fetchall():
        l.append(i)
    return(jsonify(str(l)))


if __name__ == '__main__':
    app.run()
