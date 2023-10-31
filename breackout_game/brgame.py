import turtle
import sys
import time

class BreakoutGame:
    """
    The main class for the Breakout Game.
    """
    def __init__(self):
        self.win = self.initialize_screen()
        self.paddle = self.initialize_paddle()
        self.ball = self.initialize_ball()
        self.blocks = self.initialize_blocks()
        self.setup_keyboard_input()
        self.speed_increment = 1.02
        self.max_speed = 0.6

    def initialize_screen(self):
        """
        This function initializes the gaming screen.
        """
        win = turtle.Screen()
        win.title("Breakout Game")
        win.bgcolor("black")
        win.setup(width=800, height=600)
        win.tracer(0)
        return win

    def initialize_paddle(self):
        """
        This function initializes the paddle.
        """
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=1, stretch_len=5)
        paddle.penup()
        paddle.goto(0, -250)
        return paddle

    def initialize_ball(self):
        """
        This function initializes the ball.
        """
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 0.15
        ball.dy = -0.15
        return ball

    def initialize_blocks(self):
        """
        This function initializes the blocks.
        """
        blocks = []
        colors = ["red", "green", "blue", "yellow"]
        x_start = -375
        y_start = 290
        for i in colors:
            for x in range(8):
                block = turtle.Turtle()
                block.speed(0)
                block.shape("square")
                block.color(i)
                block.shapesize(stretch_wid=1, stretch_len=3)
                block.penup()
                block.goto(x_start + 100 * x, y_start - 25 * colors.index(i))
                blocks.append(block)
        return blocks

    def move_paddle_left(self):
        """
        This function moves the paddle to the left.
        """
        x = self.paddle.xcor()
        if x > -350:
            x -= 20
            self.paddle.setx(x)

    def move_paddle_right(self):
        """
        This function moves the paddle to the right.
        """
        x = self.paddle.xcor()
        if x < 350:
            x += 20
            self.paddle.setx(x)

    def setup_keyboard_input(self):
        """
        This function sets up the keyboard input.
        """
        self.win.listen()
        self.win.onkeypress(self.move_paddle_left, "Left")
        self.win.onkeypress(self.move_paddle_right, "Right")

    def increase_ball_speed(self):
        """
        This function increases the speed of the ball.
        """
        if abs(self.ball.dx) < self.max_speed: 
            self.ball.dx *= self.speed_increment
        if abs(self.ball.dy) < self.max_speed:
            self.ball.dy *= self.speed_increment

    def detect_collision(self):
        """
        This function detects collision between the ball and the blocks or the paddle.
        """
        for block in self.blocks:
            if self.ball.distance(block) < 25:
                self.blocks.remove(block)
                block.hideturtle()
                self.ball.dy *= -1
                self.increase_ball_speed()
                break

        if self.ball.distance(self.paddle) < 50:
            self.ball.dy *= -1
            self.increase_ball_speed()

    def check_border_collision(self):
        """
        This function checks if the ball has collided with the border.
        """
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:
            self.ball.dx *= -1
        if self.ball.ycor() > 290:
            self.ball.dy *= -1

        # Game over if the ball hits the bottom
        if self.ball.ycor() < -290:
            print("Game Over!")
            time.sleep(1)
            sys.exit()

    def game_loop(self):
        """
        The main game loop.
        """
        while True:
            self.win.update()
            try:
                self.ball.setx(self.ball.xcor() + self.ball.dx)
                self.ball.sety(self.ball.ycor() + self.ball.dy)
                self.check_border_collision()
                self.detect_collision()
            except turtle.Terminator:
                print("Game Terminated")
                break
            except Exception as e:
                print("An unexpected error occurred: ", e)
                break
            finally:
                if len(self.blocks) == 0:
                    print("Congratulations, you have cleared all the blocks!")
                    print("Game Over!")
                    break

if __name__ == "__main__":
    try:
        game = BreakoutGame()
        game.game_loop()
    except Exception as e:
        print("An error occurred while running the game: ", e)