##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## controller
##

from app import app
from app.models import User, Task
from flask import render_template, request
import pymysql as sql


pwd = 'Fnzatpez1.'
user = 'root'

class Controller(object):

    def __init__(self, title, myContent):
        self.title = title
        self.myContent = myContent

    def index_action(self):
        return render_template("index.html",
                                title = self.title)

    def register_action(self):
        if request.method == 'POST':
            name = request.form['username']
            password = request.form['password']
            print(name, password)
        return render_template("register.html",
                                title = self.title)

    def display_task_action(self):
        try:
            connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')##connect to database
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM task")##execution de la requete
            result = cursor.fetchall()
            connect.commit()
            cursor.close()
            connect.close()
        except Exception as ex :
            print("Caught  an  exception : ", ex)
            result = 0
        return render_template("tasks_view.html",
                                title = self.title,
                                tables = result)

    def add_task_action(self):
        if request.method == 'POST':
            task = request.form['task']
            begin = request.form['begin']
            end = request.form['end']
            status = request.form['status']
        try:
            insert_stuff = (
                "INSERT INTO task (title, begin, end, status) VALUES ('" + task + "','" + begin + "','" + end + "','" + status + "')"
            )
            connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')##connect to database
            cursor = connect.cursor()
            cursor.execute(insert_stuff)##execution de la requete
            connect.commit()
            cursor.close()
            connect.close()
        except Exception as e :
            print("Caught  an  exception : ", e)
        return self.display_task_action()