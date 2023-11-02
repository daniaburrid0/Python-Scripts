import turtle
import random

class Brick(turtle.Turtle):
    """
    Brick class for the game.
    Inherits from turtle.Turtle class.
    """
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
    INIT_STRETCH_WID = 1
    INIT_STRETCH_LEN = 3
    
    def __init__(self, x, y, color=None):
        """Initializes the brick at coordinates (x, y) with an optional color."""
        super().__init__()
        self.shape("square")
        self.color(color if color else random.choice(self.COLORS))
        self.shapesize(stretch_wid=self.INIT_STRETCH_WID, stretch_len=self.INIT_STRETCH_LEN)
        self.penup()
        self.goto(x, y)
        self.speed(0)
        self.active = True
    
    def destroy(self):
        """Moves the brick out of visible window and deactivates it."""
        self.goto(1000, 1000)
        self.active = False

    def is_active(self):
        """Returns whether the brick is active."""
        return self.active

    def reset(self, color=None):
        """Resets the brick to its initial state with an optional new color."""
        self.goto(self.xcor(), self.ycor())
        self.color(color if color else random.choice(self.COLORS))
        self.active = True
