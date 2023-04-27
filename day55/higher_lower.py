import random

from flask import Flask

app = Flask(__name__)


def generate_random():
    return random.randint(0, 9)


r_num = generate_random()

print(r_num)


@app.route("/<int:num>")
def check_num(num):
    msg = ""
    if r_num < num:
        msg = "<h2 style='color:red'>Too High,try again ❌</h2>"
    if r_num > num:
        msg = "<h2 style='color:blue'>Too low,try again ❌</h2>"
    if r_num == num:
        msg = "<h2 style='color:green'>Gottee  🔥</h2>"
    return msg


if __name__ == "__main__":
    app.run(debug=True)
