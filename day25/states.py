import turtle
import pandas as pd

FONT = ("arial", 7, "bold")

screen = turtle.Screen()
screen.title("U.S States")
image = "./us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_cords(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cords)
# turtle.mainloop()


# todo: convert answer case
# todo: get answer state form csv
# todo: if it exists get that coords
# todo : write name on the screen on that corrds
# todo : if it not exists then input box show -> nothing else
# todo :track correct states nump
def ask_input(title):
    return screen.textinput(title = title,
                            prompt = "What's the name of his neighbor")


def write_on_screen(x, y, content):
    """
    :param x:
    :param y:
    :param content:
    :return: write on screen
    """
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(x, y)
    text.write(content, move = False, font = FONT)
    return text


is_game_complete = False
us_states = pd.read_csv("us-states-game/50_states.csv")

cor = []
while not is_game_complete:

    correct_guesses = cor
    if len(correct_guesses) > 0:
        answer = ask_input(f"{len(correct_guesses)}/{len(us_states)} States correct")
    else:
        answer = ask_input("Guess the State?")

    user_answer = answer.capitalize()

    true_state = 0
    for states in us_states:
        true_state = us_states[us_states.state == user_answer]

    if not true_state.empty:
        x = int(true_state["x"])
        y = int(true_state["y"])
        # check answer already in list
        if user_answer not in correct_guesses:
            write_on_screen(x, y, user_answer)
            cor.append(user_answer)

    if len(correct_guesses) > 50:
        is_game_complete = True

screen.mainloop()
