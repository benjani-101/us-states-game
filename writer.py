from turtle import Turtle
FONT = ("Verdana", 11, "normal")

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, align='center', font=FONT)
