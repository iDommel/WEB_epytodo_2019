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

    def __init__(self, user_id):
        self.user_id = user_id

    def index_action(self):
        return render_template("index.html")

    def register_action(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if (len(username) == 0 or len(password) == 0):
                return render_template("alerts/invalid_logs.html")
            try:
                insert_stuff = (
                    "INSERT INTO user (username, password) VALUES ('" + username + "','" + password + "')"
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
        return render_template("register.html")

    def signout_action(self):
        if self.user_id != -1:
            self.user_id = -1
            return render_template("alerts/logged_out.html", username = self.username)
        return render_template("/index.html")

    def signin_action(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if (len(username) == 0 or len(password) == 0):
                return render_template("alerts/invalid_logs.html")
            try:
                connect = sql.connect(host='localhost',
                                unix_socket='/var/lib/mysql/mysql.sock',
                                user=user,
                                passwd=pwd,
                                db='epytodo')
                cursor = connect.cursor()
                cursor.execute("SELECT * FROM user")
                result = cursor.fetchall()
                connect.commit()
                cursor.close()
                connect.close()
                for i in result:
                    if i[1] == username:
                        if i[2] == password:
                            self.user_id = i[0]
                            self.username = username
                            return render_template("alerts/logged_in.html", username = self.username)
                return render_template("alerts/invalid_logs.html")
            except Exception as ex :
                print("Caught  an  exception : ", ex)
        return render_template("signin.html")

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
                                tables = result)

    def add_task_action(self):
        if request.method == 'POST':
            task = request.form['task']
            begin = request.form['begin']
            end = request.form['end']
        try:
            if (task and begin and end):
                connect = sql.connect(host='localhost',
                                unix_socket='/var/lib/mysql/mysql.sock',
                                user=user,
                                passwd=pwd,
                                db='epytodo')
                cursor = connect.cursor()
                cursor.execute("INSERT INTO task (title, begin, end, status) VALUES ('" + task + "','" + begin + "','" + end + "','0')")
                connect.commit()
                try:
                    task_id = cursor.execute("SELECT task_id FROM task ORDER BY task_id DESC")
                    cursor.execute("INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES ('" + str(self.user_id) + "','" + str(task_id) + "')")
                except Exception as e :
                    print("Caught  an  exception : ", e)
                    print("has_task_fail")
                connect.commit()
                cursor.close()
                connect.close()
        except Exception as e :
            print("Caught  an  exception : ", e)
            print("add_task_fail")
        return self.display_task_action()