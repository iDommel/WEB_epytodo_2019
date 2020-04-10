##
## EPITECH PROJECT, 2020
## EpyToDo
## File description:
## views
##

from flask import render_template
from app import app
from  flask  import  jsonify
import  pymysql  as sql

@app.route('/user')
def route_all_users ():
    result = "Hey, it's ... ?"
    try:
        connect = sql.connect(host='localhost',
                            unix_socket='path_to_our_mysql_socket',
                            user='_user',
                            passwd='_password',
                            db='database_test1')
        cursor = connect.cursor ()
        cursor.execute("SELECT * from  user")
        result = cursor.fetchall ()
        cursor.close()
        connect.close()
    except Exception as e :
        print("Caught  an  exception : ", e)
    return jsonify(result)

@app.route('/', methods =['GET'])
def route_index ():
    return render_template("index.html",
                            title="Hello  World",
                            myContent="My SUPER  content !!")

@app.route('/index', methods =['GET'])

@app.route('/user/<username>', methods =['GET'])
def route_user(username):
    return render_template("index.html",
                            title="Hello " + username,
                            myContent="My SUPER content for " + username + "!!!")

def route_home ():
    return "Hello  world!\n"

@app.route('/user/<username>', methods =['POST'])

def route_add_user(username):
    return "User  added!\n"