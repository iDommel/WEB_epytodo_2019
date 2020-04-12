##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## controller
##

from app import app
from app.models import models
from flask import render_template, request
import pymysql as sql

class Controller(object):

    def __init__(self, user_id):
        self.models = models(user_id)

    def index_action(self):
        return render_template("index.html")

    def register_action(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if (len(username) == 0 or len(password) == 0):
                return render_template("alerts/invalid_logs.html")
            self.models.register_model(username, password)
        return render_template("register.html")

    def signout_action(self):
        if self.models.user_id != -1:
            self.models.user_id = -1
            return render_template("alerts/logged_out.html", username = self.username)
        return render_template("/index.html")

    def signin_action(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            self.username = username
            if (len(username) == 0 or len(password) == 0):
                return render_template("alerts/invalid_logs.html")
            return self.models.sign_in_model(username, password)
        return render_template("signin.html")

    def display_task_action(self):
        result = self.models.display_task_model()
        return render_template("tasks_view.html",
                                tables = result)

    def add_task_action(self):
        if request.method == 'POST':
            task = request.form['task']
            begin = request.form['begin']
            end = request.form['end']
            if (task and begin and end):
                self.models.task_create_model(task, begin, end)
        return self.display_task_action()