import random

from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager:
    def __init__(self):
        self.all_blocks = [] 

    def create_blocks(self):
        rows = 5  # Number of rows (levels)
        cols = 10  # Number of columns (blocks per row)
        x_start = -250  # Starting x-coordinate (leftmost point)
        y_start = 200  # Starting y-coordinate (top row)

        for row in range(rows):  # Loop through each row
            for col in range(cols):  # Loop through each column in the row
                new_block = Turtle(shape="square")
                new_block.speed("fastest")
                new_block.color(COLORS[row])
                new_block.penup()
                new_block.turtlesize(stretch_len=2, stretch_wid=1)  # Adjust block size

                # Calculate block position
                x_position = x_start + col * 50  # Horizontal spacing (50 pixels apart)
                y_position = y_start - row * 30  # Vertical spacing (30 pixels apart)

                new_block.goto(x_position, y_position)  # Position the block
                self.all_blocks.append(new_block)  # Add the block to the list

