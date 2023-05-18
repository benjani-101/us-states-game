from turtle import Turtle
FONT = ("Verdana", 8, "normal")

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, align='center', font=FONT)
