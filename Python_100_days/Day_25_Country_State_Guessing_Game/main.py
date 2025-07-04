import turtle
import pandas

screen = turtle.Screen()
screen.title("State Guessing Game")
image = "Python_100_days/Day_25_Country_State_Guessing_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_guessed_correctly = 0
guessed_sates = []
not_guessed_states = []
total_states = 50
state_data = pandas.read_csv("Python_100_days/Day_25_Country_State_Guessing_Game/50_states.csv")
all_states = state_data.state.to_list()

while states_guessed_correctly!= 50:

    answer_state = screen.textinput(title=f"{states_guessed_correctly}/{total_states} States Correct",prompt="Guess a State: ").title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = state_data[state_data.state == answer_state]
        new_x = state.x.item()
        new_y = state.y.item()
        t.goto(x=new_x,y=new_y)
        t.write(answer_state)
        states_guessed_correctly+=1
        guessed_sates.append(answer_state)
        
    if answer_state == "Exit":
        not_guessed_states = [state for state in all_states if state not in guessed_sates]
        df = pandas.DataFrame(not_guessed_states)
        df.to_csv("Python_100_days/Day_25_Country_State_Guessing_Game/state_not_guessed.csv")
        break

screen.exitonclick()