from flask import Flask

app = Flask(__name__)


def to_heading(fn: object) -> object:
    def rapper(*args, **kwargs):
        return f"{fn(*args,**kwargs)}{args,kwargs}"

    return rapper


@app.route("/")
@to_heading
def hello_world(name: str = "jon", tag="h2"):
    return f"<{tag}>this is created using {tag} tag by {name}</{tag}>"


if __name__ == "__main__":
    app.run(debug=True)
