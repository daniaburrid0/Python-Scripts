import turtle

class Paddle(turtle.Turtle):
    """
    Paddle class for the game.
    Inherits from turtle.Turtle class.
    """
    PADDLE_SPEED = 40
    PADDLE_LIMIT_LEFT = -340
    PADDLE_LIMIT_RIGHT = 340
    
    def __init__(self):
        """Initializes the paddle."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)
        self.speed(0)

    def move(self, direction: int):
        """
        Moves the paddle in the given direction.
        Args:
        - direction: int: -1 for left, 1 for right
        """
        new_x = self.xcor() + (direction * self.PADDLE_SPEED)
        new_x = min(max(self.PADDLE_LIMIT_LEFT, new_x), self.PADDLE_LIMIT_RIGHT)
        self.setx(new_x)

    def move_left(self):
        """Moves the paddle to the left."""
        self.move(-1)

    def move_right(self):
        """Moves the paddle to the right."""
        self.move(1)

    def reset(self):
        """Resets the paddle position."""
        self.goto(0, -250)
