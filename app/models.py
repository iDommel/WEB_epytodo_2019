##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## models
##

import pymysql as sql
from flask import render_template

pwd = 'sdfmovieconquest1'
user = 'root'

class Models(object):

    def __init__(self, user_id):
        self.user_id = user_id

    def task_create_model(self, task, begin, end):
        try:
            connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')
            cursor = connect.cursor()
            cursor.execute("INSERT INTO task (title, begin, end, status) VALUES ('" + task + "','" + begin + "','" + end + "','0')")
            connect.commit()
            try:
                cursor.execute("SELECT task_id FROM task ORDER BY task_id DESC")
                task_id = (cursor.fetchall())[0][0]
                cursor.execute("INSERT INTO user_has_task (fk_user_id, fk_task_id) VALUES ('" + str(self.user_id) + "','" + str(task_id) + "')")
            except Exception as e :
                print("Caught  an  exception : ", e)
                print("'has_task' fail")
            connect.commit()
            cursor.close()
            connect.close()
        except Exception as e :
            print("Caught  an  exception : ", e)
            print("'add_task' fail")

    def register_model(self, username, password):
        try:
            insert_stuff = ("INSERT INTO user (username, password) VALUES ('" + username + "','" + password + "')")
            connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')
            cursor = connect.cursor()
            cursor.execute("SELECT username FROM user")
            select = cursor.fetchall()
            for elem in select:
                if elem[0] == username:
                    cursor.close()
                    connect.close()
                    print (username + " ? " + elem[0])
                    return render_template("alerts/invalid_logs_reg.html", username = username)
            cursor.execute(insert_stuff)
            connect.commit()
            cursor.close()
            connect.close()
            return render_template("register.html")
        except Exception as e :
            print("Caught  an  exception : ", e)
            return render_template("alerts/invalid_logs_reg.html", username = username)

    def display_task_model(self):
        try:
            connect = sql.connect(host='localhost',
                            unix_socket='/var/lib/mysql/mysql.sock',
                            user=user,
                            passwd=pwd,
                            db='epytodo')
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM user_has_task")
            user_and_task_id_tab = cursor.fetchall()
            cursor.execute("SELECT * FROM task")
            tasks_tab = cursor.fetchall()
            task_id_tab = []
            for elem in user_and_task_id_tab:
                if (elem[0] == self.user_id):
                    task_id_tab.append(elem)
            result = []
            for elem in task_id_tab:
                for task in tasks_tab:
                    if elem[1] == task[0]:
                        result.append(task)
            connect.commit()
            cursor.close()
            connect.close()
            return result
        except Exception as ex :
            print("Caught  an  exception : ", ex)
            return 0

    def sign_in_model(self, username, password):
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
                        return render_template("alerts/logged_in.html", username = username)
            return render_template("alerts/invalid_logs.html", username = username)
        except Exception as ex :
            print("Caught  an  exception : ", ex)
            return render_template("signin.html", username = username)