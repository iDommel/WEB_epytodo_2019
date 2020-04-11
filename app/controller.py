##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## controller
##

from app import *
from app.models import *
from flask import render_template

class Controller(object):

    def __init__(self, title, myContent):
        self.title = title
        self.myContent = myContent

    def index_action(self):
        return render_template("index.html",
                            title = self.title,
                            myContent = self.myContent)

    def register_action(self):
        return render_template("register.html",
                            title = self.title,
                            myContent = self.myContent)