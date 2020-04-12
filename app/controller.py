##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## controller
##

from app import app
from app.models import User, Task
from flask import render_template, request

class Controller(object):

    def __init__(self, title, myContent):
        self.title = title
        self.myContent = myContent

    def index_action(self):
        return render_template("index.html",
                                title = self.title,
                                )

    def register_action(self):
        if request.method == 'POST':
            name = request.form['name']
            password = request.form['password']
            print(name, password)
        return render_template("register.html",
                                title = self.title)