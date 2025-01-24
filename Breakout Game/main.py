
from turtle import Screen
from player import Player
from block_manager import BlockManager
from chancesboard import Chancesboard
from ball import Ball
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")  # Set background color for better visibility
screen.tracer(0) 



def hold_left():
    global move_left_active
    if move_left_active:
        player.move_left()
        screen.ontimer(hold_left, 30)  # Repeatedly call `hold_left` every 50 ms


def hold_right():
    global move_right_active
    if move_right_active:
        player.move_right()
        screen.ontimer(hold_right, 30)  # Repeatedly call `hold_right` every 50 ms


def start_move_left():
    global move_left_active
    move_left_active = True
    hold_left()  # Start calling `hold_left`


def stop_move_left():
    global move_left_active
    move_left_active = False  # Stop movement


def start_move_right():
    global move_right_active
    move_right_active = True
    hold_right()  # Start calling `hold_right`


def stop_move_right():
    global move_right_active
    move_right_active = False  # Stop movement



blocks = BlockManager()
player = Player()
ball = Ball()
score = Scoreboard()
chance = Chancesboard()

blocks.create_blocks()

game_is_on = True
speed = 10
direction = random.randint(20,120)
ball.setheading(direction)

while game_is_on:
    ball.move_ball(5)
   
    if ball.xcor() > 290:
        ball.bounce()

    if ball.xcor() < -290:
        ball.bounce()

    if ball.ycor() > 290:
        ball.bounce()

    if ball.ycor() < -300:
        chance.minus()
        ball.reset_position()

        
    if chance.player_chances == 0:
        game_is_on = False
        chance.gameover()

    for block in blocks.all_blocks: 
        if ball.distance(block) < 25:
            ball.bounce_off_block()
            block.goto(1000, 1000)
            score.record()

            
            # block.hideturtle()
            
            # block.clear()
    if len(blocks.all_blocks) == 0:
        chance.winner()

    if ball.distance(player) < 50:
        ball.bounce_off_paddle()
        




    screen.listen()
    move_left_active = False
    move_right_active = False

    # Key press and release bindings
    screen.onkeypress(start_move_left, "Left")
    screen.onkeyrelease(stop_move_left, "Left")
    screen.onkeypress(start_move_right, "Right")
    screen.onkeyrelease(stop_move_right, "Right")

    screen.update()

screen.exitonclick()