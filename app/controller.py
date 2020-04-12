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


pwd = 'sdfmovieconquest1'
user = 'root'

class Controller(object):

    def __init__(self, title, myContent):
        self.title = title
        self.user_id = 1

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
                            db='epytodo')
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM task")
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
        try:
            insert_stuff = (
                "INSERT INTO task (title, begin, end, status) VALUES ('" + task + "','" + begin + "','" + end + "','0')"
            )
            connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')
            cursor = connect.cursor()
            cursor.execute(insert_stuff)
            connect.commit()
            cursor.close()
            connect.close()
        except Exception as e :
            print("Caught  an  exception : ", e)
        try:
                connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')
                cursor = connect.cursor()
                task_id = cursor.execute("SELECT task_id FROM task ORDER BY task_id DESC")
                cursor.execute("INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES ('" + str(self.user_id) + "','" + task_id + "')")
                connect.commit()
                cursor.close()
                connect.close()
        except Exception as e :
            print("Caught  an  exception : ", e)
        return self.display_task_action()