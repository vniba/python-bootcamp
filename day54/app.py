from flask import Flask

app: Flask = Flask(__name__)

print(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1>"


@app.route("/x")
def x():
    return "<p style='color:red'>Copyright (c) 2023</p>"


@app.route("/n/<user_name>/<int:n>")
def greet(user_name, n=0):
    return f"Hello > {user_name} {n * 10}"


# if __name__ == "__main__":
#     app.run(debug=True)
