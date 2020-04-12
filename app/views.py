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
control = Controller(-1)

@app.route('/', methods =['GET'])
def route_index ():
    return control.index_action()

@app.route('/register', methods =['POST', 'GET'])
def route_register():
    return control.register_action()

@app.route('/signin', methods =['POST', 'GET'])
def route_signin ():
    return control.signin_action()

@app.route('/signout', methods =['POST'])
def route_signout ():
    return control.index_action()

@app.route('/user', methods =['GET'])
def route_all_users ():
    return control.index_action()

@app.route('/user/task', methods =['GET'])
def route_view_tasks():
    return control.display_task_action()

@app.route('/user/task/id', methods =['GET'])
def route_view_specific_task():
    return control.index_action()

@app.route('/user/task/id', methods =['POST'])
def route_update_specific_task():
    return control.index_action()

@app.route('/user/task/add', methods =['POST'])
def route_add_task():
    return control.add_task_action()

@app.route('/user/task/del/id', methods =['POST'])
def route_del_task():
    return control.index_action()