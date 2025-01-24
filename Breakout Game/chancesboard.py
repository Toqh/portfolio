FONT = ("Courier", 10, "normal")

from turtle import Turtle
class Chancesboard(Turtle):
        def __init__(self):
            super().__init__()
            self.player_chances = 10
            self.hideturtle()
            self.penup()
            self.color("black")
            self.goto(200, 280)
            self.write(f"Lives:{self.player_chances}", align="center", font=FONT)

        def minus(self):
            self.player_chances -= 1
            self.clear()
            self.write(f"Lives:{self.player_chances}", align="center", font=FONT)
        

        def gameover(self):
            self.penup()
            self.goto(0, 0)
            self.write(f"Game over", align="center", font=FONT)
        
        def winner(self):
            self.penup()
            self.goto(0, 0)
            self.write(f"You win", align="center", font=FONT)







