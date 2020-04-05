from . import app, db
from flask import request, render_template, jsonify, redirect, url_for
import requests
from random import *
from .models import Projects, Contacts


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    response={
        'randomNumber':randint(1,100)
    }
    return jsonify(response)

@app.route('/api/projects')
def projects():
    response = []
    for i in Projects.query.all():
        item ={ "title":i.title, "description":i.description, "logo":i.logo, "date":i.date}
        response.append(item)

    return jsonify(response)


@app.route('/api/navbar/items')
def nav_items():
    pass

@app.route('/api/newproject', methods=["GET","POST"])
def new_project():
    if request.method == "POST":
        data =request.get_json(silent=True)
        title = data[0].get('content')
        description = data[1].get('content')
        logo = data[2].get('content')
        date = data[3].get('content')
        newProject = Projects(title=title,description=description,logo=logo,date=date)
        db.session.add(newProject)
        db.session.commit()
    return "200"

@app.route('/api/contact', methods=["GET","POST"])
def contact():

    if request.method == "POST":
        data =request.get_json(silent=True)
        newContact = Contacts(name=data[0], email=data[1], from_where=data[2], msg=data[3])
        db.session.add(newContact)
        db.session.commit()
    return "200"



