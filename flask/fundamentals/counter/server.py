from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "UcEsM9TWsF.!CbnK2w*s"

counter = 0
userVisits = 0

@app.route('/')
@app.route('/<int:plus>')
def index(plus = 1):
    c = 'counter'
    if c in session:
        session[c] += plus
    else:
        session[c] = 1

    return render_template("index.html", counter=session[c])

@app.route('/custom', methods=['POST'])
def custom():
    return redirect(f"/{request.form['custNum']}")

@app.route('/destroy_session')
def create_user():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def fourZeroFour(err):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)