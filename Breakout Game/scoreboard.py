FONT = ("Courier", 10, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.player_score = 0
            self.hideturtle()
            self.penup()
            self.color("black")
            self.goto(-200, 280)
            self.write(f"LScore:{self.player_score}", align="center", font=FONT)

        def record(self):
            self.player_score += 10
            self.clear()
            self.write(f"Score:{self.player_score}", align="center", font=FONT)
  

