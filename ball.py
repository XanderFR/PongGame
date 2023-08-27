from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.color("gold")
        self.penup()

        # Initial ball x and y axis movement values
        self.xMove = 10
        self.yMove = 10

        self.moveSpeed = 0.1

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    def bounceY(self):
        # Change y-axis movement value to negative
        self.yMove *= -1

    def bounceX(self):
        # Change x-axis movement value to negative
        self.xMove *= -1
        self.moveSpeed *= 0.9  # increases ball speed on paddle contact

    def resetPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1  # reset ball speed
        self.bounceX()  # Changes ball direction every round
