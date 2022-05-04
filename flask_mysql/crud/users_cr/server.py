from flask import Flask, redirect, render_template, request
# import the class from user.py
from users import User
app = Flask(__name__)

@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/create')
def add():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
    "fname" : request.form['fname'],
    "lname" : request.form['lname'],
    "email" : request.form['email']
}

    User.save(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)