from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.setposition(0, 0)
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10
        self.speed = 1
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1   # goes backwards (it's like - self.y_move /// - 10)
        self.move_speed *= 0.9

    def bounce_x(self):
        """this function shows when one paddle hit the ball and then bounces the ball back + increases speed of ball"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



