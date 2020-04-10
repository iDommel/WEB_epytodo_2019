##
## EPITECH PROJECT, 2020
## EpyToDo
## File description:
## views
##

from flask import render_template
from app import app
from  flask  import  jsonify
import  pymysql  as sql

user='root'


@app.route('/user')
def route_all_users ():
    try:
        insert_stuff = (
            "INSERT INTO user (username, password)\
            VALUES ('bob','bob')"
        )
        connect = sql.connect(host='localhost',
                        unix_socket='/var/lib/mysql/mysql.sock',
                        user=user,
                        passwd='Fnzatpez1.',
                        db='new_schema')##connectionbd
        cursor = connect.cursor ()##ini de la requete
        cursor.execute(insert_stuff)##execution de la requete
        cursor.execute("SELECT * FROM user")##execution de la requete

        result = cursor.fetchall()
        connect.commit()
        cursor.close()
        connect.close()
    except Exception as e :
        print("Caught  an  exception : ", e)
        result = 0
    return jsonify(result)


@app.route('/', methods =['GET'])
def route_index ():
    return render_template("index.html",
                            title="Index",
                            myContent="My SUPER  content !!")

@app.route('/form', methods =['GET'])
def route_form():
    return render_template("form.html",
                            title="FORM !!!!!!",
                            myContent="My SUPER FUCKING content !!")

@app.route('/user/<username>', methods =['GET'])
def route_user(username):
    return render_template("index.html",
                            title="Hello " + username,
                            myContent="My SUPER content for " + username + "!!!")

def route_home ():
    return "Hello  world!\n"

@app.route('/user/<username>', methods =['POST'])

def route_add_user(username):
    return "User  added!\n"