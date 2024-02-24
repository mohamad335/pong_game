from turtle import *
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_factor = 0.1
        self.x = 10
        self.y = 10
    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce(self):
        self.y *= -1
        self.move_factor *= 0.9
    def bounce_y(self):

        self.x *= -1

    def direction(self):
        self.goto(0, 0)
        self.move_factor = 0.1
        self.bounce_y()



















