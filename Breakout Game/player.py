STARTING_POSITION = (0, -280)

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(STARTING_POSITION)
        self.turtlesize(stretch_len=5, stretch_wid=1) 

    def create_player(self):
        pass  # This method is now empty as the initialization is done in __init__

    def move_left(self):
        if self.xcor() > -280:
            new_x = self.xcor() - 30
            self.setx(new_x)

    def move_right(self):
        if self.xcor() < 280:
            new_x = self.xcor() + 30
            self.setx(new_x)
    # def left(self):
    #     self.current_y = self.xcor()
    #     self.sety(self.current_y - 20)

    # def right(self):
    #     self.current_y = self.xcor()
    #     self.sety(self.current_y + 20)

    def reset_position(self):
        self.setposition(STARTING_POSITION)
