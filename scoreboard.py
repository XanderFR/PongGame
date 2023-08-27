from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()  # Prepares scoreboard for new numbers

        # left side of scoreboard
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 80, "normal"))

        # right side of scoreboard
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 80, "normal"))

    def lPoint(self):
        self.lScore += 1
        self.updateScoreboard()

    def rPoint(self):
        self.rScore += 1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0, 0)
        # Check the scores and name the winner
        if self.lScore > self.rScore:
            self.write("Left Paddle is the WINNER!", align="center", font=("Courier", 20, "normal"))
        else:
            self.write("Right Paddle is the WINNER!", align="center", font=("Courier", 20, "normal"))
