from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

HIGHEST_SCORE = 5

# Screen initialization
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # turn off automatic screen updates

# Paddle initialization
lPaddle = Paddle((-350, 0), "red")  # left paddle is red
rPaddle = Paddle((350, 0), "blue")  # right paddle is blue

# Ball initialization
ball = Ball()

# Scoreboard initialization
scoreboard = Scoreboard()

# Game controls
screen.listen()
screen.onkey(rPaddle.goUp, "Up")
screen.onkey(rPaddle.goDown, "Down")
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")

# Game loop
gameOn = True
while gameOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # If ball collides with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # If ball collides with right paddle
    if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # If right paddle misses ball
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.lPoint()

    # If left paddle misses ball
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rPoint()

    # A way to win the game
    if scoreboard.lScore == HIGHEST_SCORE or scoreboard.rScore == HIGHEST_SCORE:
        gameOn = False
        scoreboard.gameOver()

screen.exitonclick()
