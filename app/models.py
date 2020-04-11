##
## EPITECH PROJECT, 2020
## WEB_epytodo_2019
## File description:
## models
##

class User(object):

    def __init__(self):
        self.table = "user"
        self.fk = "user_has_task"

    def create(self, username, password):
        something = 0

class Task(object):

    def __init__(self):
        self.table = "task"
        self.fk = "user_has_task"

    def create(self, user_id, title, begin, end):
        something = 0