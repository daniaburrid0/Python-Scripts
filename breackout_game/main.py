import turtle
from entities.ball import Ball
from entities.paddle import Paddle
from entities.brick import Brick

# Create the game window
window = turtle.Screen()
window.title("Breakout")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Initialize score and lives
score = 0
lives = 3

# Score and Lives display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

# Create the paddle, ball, and bricks
paddle = Paddle()
ball = Ball()
bricks = []

# Function to reset bricks and re-add to the game, invoked for a complete game reset
def reset_bricks():
    global bricks
    for brick in bricks:
        brick.destroy()
    bricks.clear()
    for i in range(4):
        for j in range(8):
            brick = Brick(-280 + j * 80, 250 - i * 40)
            bricks.append(brick)

# Initialize bricks
reset_bricks()

# Function to move the paddle left
def move_paddle_left():
    paddle.move_left()

# Function to move the paddle right
def move_paddle_right():
    paddle.move_right()

# Keyboard bindings
window.listen()
window.onkeypress(move_paddle_left, "Left")
window.onkeypress(move_paddle_right, "Right")

# Main game loop
while True:
    window.update()
    
    # Move the ball
    ball.move()

    # Check for collision with the paddle
    if ball.collides_with(paddle):
        ball.bounce_off_paddle(paddle)

    # Check for collision with bricks
    for brick in bricks:
        if ball.collides_with(brick):
            brick.destroy()
            bricks.remove(brick)
            ball.bounce_off_brick(brick)
            
            # Update score
            score += 10
            score_display.clear()
            score_display.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    # Check for game over
    if ball.ycor() < -290:
        lives -= 1
        if lives > 0:
            ball.reset()
            paddle.reset()
        else:
            # Complete game reset
            score_display.clear()
            score_display.write("Game Over", align="center", font=("Courier", 24, "normal"))
            window.update()
            break  # Break the game loop to terminate

        score_display.clear()
        score_display.write("Score: {} Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

window.bye()  # Close the window when the game is over
