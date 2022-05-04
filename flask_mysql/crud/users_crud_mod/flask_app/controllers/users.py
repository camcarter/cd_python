from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/users/new')
def add():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
    "fname" : request.form["fname"],
    "lname" : request.form["lname"],
    "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route('/read')
def read_one():
    return render_template('read_one.html')

@app.route('/users/edit')
def edit(x):
    data = {'id' : x}
    User.edit_user(data)
    return render_template('edit.html')

@app.route('/edit_user', methods=["POST"])
def edit_user(x):
    data = {
    "fname" : request.form["fname"],
    "lname" : request.form["lname"],
    "email" : request.form["email"],
    "id"    : x
    }
    User.edit_user(data)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {'id' : id}
    User.del_user(data)
    return redirect('/users')