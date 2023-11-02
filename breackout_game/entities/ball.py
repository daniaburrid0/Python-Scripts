import turtle
from .brick import Brick
from .paddle import Paddle

class Ball(turtle.Turtle):
    """
    Ball class for the game.
    Inherits from turtle.Turtle class.
    """
    INIT_X = 0
    INIT_Y = -200
    INIT_DX = 1
    INIT_DY = -1
    
    def __init__(self):
        """Initializes the ball."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(self.INIT_X, self.INIT_Y)
        self.speed(0)
        self.dx = self.INIT_DX
        self.dy = self.INIT_DY

    def move(self):
        """Moves the ball."""
        self._wall_collision()
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def _wall_collision(self):
        """Checks for collision with walls and bounces off if needed."""
        if self.xcor() > 390 or self.xcor() < -390:
            self.dx *= -1
        if self.ycor() > 290:
            self.dy *= -1

    def collides_with(self, other):
        """
        Determines if the ball collides with other game elements.
        Args:
        - other: Either Brick or Paddle object
        """
        distance = self.distance(other)
        if isinstance(other, Brick) and distance < 30:
            return True
        elif isinstance(other, Paddle) and distance < 40:
            return True
        return False

    def bounce_off_paddle(self, paddle: Paddle):
        """Changes the direction upon hitting the paddle."""
        self.dy *= -1
        distance = self.xcor() - paddle.xcor()
        self.dx = distance / 20

    def bounce_off_brick(self, brick: Brick):
        """Changes the direction upon hitting a brick."""
        self.dy *= -1

    def reset(self):
        """Resets the ball to its initial state."""
        self.goto(self.INIT_X, self.INIT_Y)
        self.dx = self.INIT_DX
        self.dy = self.INIT_DY
