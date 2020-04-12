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
                                db='epytodo')##connect to database
                cursor = connect.cursor()
                cursor.execute(insert_stuff)##execution de la requete
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
                                db='epytodo')##connect to database
                cursor = connect.cursor()
                cursor.execute("SELECT * FROM user")##execution de la requete
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
        else:
            return render_template("signin.html")

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