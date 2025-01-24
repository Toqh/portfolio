from turtle import Turtle
from random import Random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.speed(0)
        self.pencolor("black")
        self.penup()
        

    def move_ball(self,speed):
        self.forward(speed)


    def bounce(self):
        if self.xcor() > 280:  # Right wall
            self.setheading(180 - self.heading()) 
        elif self.xcor() < -280:  # Left wall
            self.setheading(180 - self.heading())
        elif self.ycor() > 280:  # Top wall
            self.setheading(-self.heading()) 

    def bounce_off_block(self):
        self.current_heading = self.heading()
        self.setheading(self.current_heading + 90)
        
    def bounce_off_paddle(self):
        self.setheading(-self.heading())
   
    def reset_position(self):
        self.setposition(0,0)