import turtle
import pandas as pd

FONT = ("arial", 7, "bold")

screen = turtle.Screen()
screen.title("U.S States")
image = "./us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("us-states-game/50_states.csv")
all_state = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer = screen.textinput(title = f"{len(guessed_states)}/ 50 States correct",
                              prompt = "What's the name of his neighbor").title()

    if answer == "Exit":
        new_l = []
        # all states that not guessed by user
        for state in all_state:
            if state not in guessed_states:
                new_l.append(state)
        # convert to dataframe and csv
        learn_s = pd.DataFrame(new_l, columns = ["state"])
        learn_s.to_csv("states_to_learn.csv")
        break

    if answer in all_state:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.y), int(state_data.y))
        t.write(state_data.state.item())
