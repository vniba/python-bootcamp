from flask import Flask

app = Flask(__name__)


def logging_decorator(fn: object) -> object:
    def rapper():
        return f"{fn.__name__} {fn()}"

    return rapper


@app.route("/")
@logging_decorator
def liar():
    return f"<li>liar</li>"


if __name__ == "__main__":
    app.run(debug=True)
