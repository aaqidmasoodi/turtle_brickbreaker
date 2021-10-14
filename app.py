import turtle
import time
import random
# GAME VARIABLES
FPS = 1/120
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



# my screen
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.title('BrickBreaker - CodeWithAaqid')
screen.bgcolor('lightgray')
screen.tracer(0)



# ball 
ball = turtle.Turtle()
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.speed(0)
ball.goto(0, -SCREEN_HEIGHT//2 + 100)
ball.velocity = 3
ball.dx = ball.velocity
ball.dy = ball.velocity


# paddle
paddle = turtle.Turtle()
paddle.shape('square')
paddle.penup()
paddle.goto(0,-(SCREEN_HEIGHT//2) + 50)
paddle.color('maroon')
paddle.SCALE_X = 7
paddle.SCALE_Y = 1.2
paddle.shapesize(stretch_len=paddle.SCALE_X, stretch_wid=paddle.SCALE_Y)
paddle.speed(0)
paddle.change = 40




# bricks
bricks = []
brick_rows = 3
brick_cols = SCREEN_WIDTH // 100
top_left = (-(SCREEN_WIDTH//2) + 50,(SCREEN_HEIGHT//2) - 20)
brick_coordinates = []


for col in range(brick_rows):
	y_offset = col * 40
	for row in range(SCREEN_WIDTH//100):
		x_offset = row * 100
		brick_coordinates.append((top_left[0] + x_offset,top_left[1] - y_offset))



# print(type(top_left[0]))

for i in range(brick_rows * brick_cols):
	bricks.append(turtle.Turtle())

for index, brick in enumerate(bricks):
	brick.shapesize(stretch_len=5,stretch_wid=2)
	brick.shape('square')
	brick.color('purple')
	brick.penup()
	brick.speed(0)
	brick.goto(brick_coordinates[index])






# checking collisions
def top_collisions():
	'''
		this functions check whether the ball 
		has collided with the top and the bottom screen.
		returns True if it has.
	'''
	top_conditions = [
		ball.ycor() > SCREEN_HEIGHT//2 - 10,
	]

	if any(top_conditions):
		return True

	return False


def left_right_collisions():
	'''
		this functions check whether the ball 
		has collided with the left and the right screen.
		returns True if it has.
	'''
	left_right_conditions = [
		ball.xcor() > SCREEN_WIDTH//2 - 10,
		ball.xcor() < -SCREEN_WIDTH//2 + 10,
	]

	if any(left_right_conditions):
		return True

	return False



def ball_colliding_paddle():

	collision_conditions = [
		ball.xcor() < paddle.xcor() + ((paddle.SCALE_X * 10) + 10),
		ball.xcor() > paddle.xcor() - ((paddle.SCALE_X * 10) + 10),
		ball.ycor() < paddle.ycor() + ((paddle.SCALE_Y * 10) + 10),
		ball.ycor() > paddle.ycor() - ((paddle.SCALE_Y * 10) + 10),
	]

	if all(collision_conditions):
		return True

	return False


def ball_on_left_or_right_of_paddle():

	left_right_conditions = [
		ball.xcor() > paddle.xcor() + (paddle.SCALE_X * 10),
		ball.xcor() < paddle.xcor() - (paddle.SCALE_X * 10),
	]

	if any(left_right_conditions):
		return True

	return False


def ball_on_top_or_bottom_of_paddle():

	top_bottom_conditions = [
		ball.ycor() > paddle.ycor() + (paddle.SCALE_Y * 10),
		ball.ycor() < paddle.ycor() - (paddle.SCALE_Y * 10),
	]

	if any(top_bottom_conditions):
		return True

	return False


def ball_colliding_brick():
	collision_conditions = [
		ball.xcor() < brick.xcor() + 60,
		ball.xcor() > brick.xcor() - 60,
		ball.ycor() < brick.ycor() + 20,
		ball.ycor() > brick.ycor() - 20,
	]

	if all(collision_conditions):
		return True

	return False


def ball_on_left_or_right_of_brick(brick):

	left_right_conditions = [
		ball.xcor() > brick.xcor() + 50,
		ball.xcor() < brick.xcor() - 50,
	]

	if any(left_right_conditions):
		return True

	return False


def ball_on_top_or_bottom_of_brick(brick):

	top_bottom_conditions = [
		ball.ycor() > brick.ycor() + 10,
		ball.ycor() < brick.ycor() - 10,
	]

	if any(top_bottom_conditions):
		return True

	return False



# Moving the paddle left and right
def paddle_left():
	paddle.setx(paddle.xcor() - paddle.change)

def paddle_right():
	paddle.setx(paddle.xcor() + paddle.change)

# Event Binding
screen.listen()
screen.onkeypress(paddle_left, 'a')
screen.onkeypress(paddle_right, 'd')









# Main Game Loop
while True:

	# Moving the ball
	ball.setx(ball.xcor() + ball.dx) # change the x coordinate
	ball.sety(ball.ycor() + ball.dy) # change the y coordinate



	# top collisions 
	if top_collisions():
		ball.dy *= -1

	# Respawn
	if ball.ycor() < -SCREEN_HEIGHT//2 - 20:
		ball.dy *= -1
		ball.goto(0,-200)

	# left and right collisions
	if left_right_collisions():
		ball.dx *= -1



	# paddle and ball collisions

	if ball_colliding_paddle():
		if ball_on_left_or_right_of_paddle():
			ball.dx *= -1

		elif ball_on_top_or_bottom_of_paddle():
			ball.dy *= -1



	for brick in bricks:
		
		if ball_colliding_brick():
			
			if ball_on_left_or_right_of_brick(brick):
				ball.dx *= -1
				brick.hideturtle()
				bricks.remove(brick)

			elif ball_on_top_or_bottom_of_brick(brick):
				ball.dy *= -1
				brick.hideturtle()
				bricks.remove(brick)




	# Auto
	paddle.setx(ball.xcor())


	# updating the screen
	screen.update()
	time.sleep(FPS)