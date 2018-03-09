import pygame
import sys
import random

pygame.init()
canvas_width, canvas_height = 1000, 500
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption('Bricks')
fps_clock = pygame.time.Clock()
FPS = 40

white = pygame.Color('white')
black = pygame.Color('black')
colors = [pygame.Color(10 * random.randint(1, 25), 10 * random.randint(1, 25), 10 * random.randint(1, 25)) for x in range(10)]

paddle_width, paddle_height, paddle_color = 80, 20, black
ball_radius, ball_color = 10, black
ball_direction_x, ball_direction_y = 5, 5

# if true makes it so the paddle keeps moving even if the key is not pressed
continuous_move = False
move = 0 if continuous_move == False else 10

class Ball:
	def __init__(self, radius):
		self.radius = radius
		# need int to draw circle
		self.x = int(canvas_width/3)
		self.y = int(canvas_height/2)

	def reset(self):
		self.x = int(canvas_width/3)
		self.y = int(canvas_height/2)

	def rectangle(self):
		return pygame.Rect(self.x, self.y, self.radius, self.radius)

	def draw(self):
		pygame.draw.circle(canvas, ball_color, (self.x, self.y), self.radius)

class Brick:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = random.choice(colors)

	def rectangle(self):
		return pygame.Rect(self.x, self.y, self.width + 10, self.height + 10)

	def draw(self):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))

class Paddle(Brick):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.x = canvas_width/2 - self.width/2
		self.y = canvas_height - self.height - 10
		self.color = paddle_color

def wall_bounce(ball):
	global ball_direction_x
	global ball_direction_y
	if ball.x - ball.radius <= 0 or ball.x + ball.radius >= canvas_width:
		ball_direction_x *= -1
	elif ball.y - ball.radius <= 0:
		ball_direction_y *= -1
	elif ball.y + ball.radius >= canvas_height:
		ball.reset()

def paddle_bounce(ball, paddle):
	global ball_direction_y
	if ball.rectangle().colliderect(paddle.rectangle()) == True:
		ball_direction_y *= -1

def brick_bounce(ball, brick):
	global ball_direction_x
	global ball_direction_y
	if ball.rectangle().colliderect(brick.rectangle()):
		ball_direction_y *= -1
		return True

def brick_grid(width, height, brick_width=50, brick_height=15, spacer=5):
	# returns a grid which is width bricks wide and height bricks high
	return [[Brick(x * brick_width + spacer * x, y * brick_height + spacer * y, brick_width, brick_height) for x in range(width)] for y in range(height)]

def draw_grid(ball, grid):
	for line in grid:
		for b in line:
			b.draw()

def check_grid(ball, grid):
	for line in grid:
		for i, b in enumerate(line):
			if brick_bounce(ball, b):
				del line[i]

bg = brick_grid(19, 4)

paddle = Paddle(paddle_width, paddle_height)

ball = Ball(ball_radius)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move = -10
			elif event.key == pygame.K_RIGHT:
				move = 10
		if continuous_move == False:
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					move = 0
				elif event.key == pygame.K_RIGHT:
					move = 0

	draw_grid(ball, bg)
	check_grid(ball, bg)
	wall_bounce(ball)
	paddle_bounce(ball, paddle)

	paddle.draw()
	ball.draw()

	paddle.x += move
	ball.x += ball_direction_x
	ball.y += ball_direction_y

	pygame.display.update()
	fps_clock.tick(FPS)
	canvas.fill(white)



pygame.quit()