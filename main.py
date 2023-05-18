import turtle
import pandas as pd
from writer import Writer

state_map_file = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title('US States Game')
# adds map to screen
screen.addshape(state_map_file)
turtle.shape(state_map_file)
# initialize writer
writer = Writer()
# get dataframe from csv
df = pd.read_csv('50_states.csv')


playing = True
score = 0
correct_answers = []
while playing:
    answer_state = screen.textinput(title=f"Guess state: {score}/50", prompt="Guess the state:").title()
    if answer_state in df['state'].tolist() and answer_state not in correct_answers:
        row = df[df['state'] == answer_state]
        x = int(row['x'].iloc[0])
        y = int(row['y'].iloc[0])
        writer.write_state(answer_state, x, y)
        score += 1
        correct_answers.append(answer_state)



screen.mainloop()