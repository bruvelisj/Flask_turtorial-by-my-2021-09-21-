from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome, world!"

@app.route("/Hi")
def hi_world():
    return "Hi, World!"

@app.route("/user/<username>")
def user(username):
    return "Welcome user: %s" % escape(username)

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("asd.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)