##
## EPITECH PROJECT, 2020
## EpyToDo
## File description:
## views
##

from flask import Flask, render_template, jsonify, request
from app import app
from app.controller import Controller
import pymysql as sql

app.config['SECRET_KEY'] = 'codex'

@app.route('/', methods =['GET'])
def route_index ():
    control = Controller("Home", "Index content")
    return control.index_action()

@app.route('/register', methods =['GET', 'POST'])
def route_register():
    control = Controller("Register Page", "register.html")
    return control.register_action()

@app.route('/signin', methods =['POST'])
def route_signin ():
    control = Controller("Signin Page", "Signin content")
    return control.index_action()

@app.route('/signout', methods =['POST'])
def route_signout ():
    control = Controller("Signout Page", "Signout content")
    return control.index_action()

@app.route('/user', methods =['GET'])
def route_all_users ():
    try:
        user = 'root'
        insert_stuff = (
            "INSERT INTO user (username, password)\
            VALUES ('name','mdp')"
        )
        connect = sql.connect(host='localhost',
                        unix_socket='/var/lib/mysql/mysql.sock',
                        user=user,
                        passwd='sdfmovieconquest1',
                        db='epytodo')##connect to database
        cursor = connect.cursor()
        cursor.execute(insert_stuff)##execution de la requete
        cursor.execute("SELECT * FROM user")##execution de la requete

        result = cursor.fetchall()
        connect.commit()
        cursor.close()
        connect.close()
    except Exception as e :
        print("Caught  an  exception : ", e)
        result = 0
    return jsonify(result)

@app.route('/user/task', methods =['GET'])
def route_view_tasks():
    control = Controller("Tasks Page", "Your tasks")
    return control.display_task_action()

@app.route('/user/task/id', methods =['GET'])
def route_view_specific_task():
    control = Controller("Task Page", "A task")
    return control.index_action()

@app.route('/user/task/id', methods =['POST'])
def route_update_specific_task():
    control = Controller("Task Page", "Update a task")
    return control.index_action()

@app.route('/user/task/add', methods =['POST'])
def route_add_task():
    control = Controller("Task Page", "Add task")
    return control.add_task_action()

@app.route('/user/task/del/id', methods =['POST'])
def route_del_task():
    control = Controller("Task Page", "Del task")
    return control.index_action()