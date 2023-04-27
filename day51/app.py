from flask import Flask

app: Flask = Flask(__name__)

print(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1>"


@app.route("/x")
def x():
    return "<p>Copyright (c) 2023</p>"


if __name__ == "__main__":
    app.run()
