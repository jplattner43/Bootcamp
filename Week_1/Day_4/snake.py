import pygame
import sys
import random

pygame.init()
canvas = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake')
white = pygame.Color('white')
blue = pygame.Color('blue')
red = pygame.Color('red')
black = pygame.Color('black')
green = pygame.Color('green')
canvas.fill(white)
direction = 'right'
snake_body = [[180, 150], [190, 150], [200, 150]]
x = 0
FPS = 10
fps_clock = pygame.time.Clock()
lives = 3
score = 0

class Food:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw_food(self):
		pygame.draw.circle(canvas, red, (self.x, self.y), 5)

def food_collision(snake, snack):
	# checks with the middle of the front of the head
	if direction == 'up' or direction == 'down':
		if (snack.x - 10 < snake[-1][0] + 5 < snack.x + 10) and (snack.y - 10 < snake[-1][1] < snack.y + 10):
			return True
	elif direction == 'right':
		if (snack.x - 10 < snake[-1][0] + 10 < snack.x + 10) and (snack.y - 10 < snake[-1][1] + 5 < snack.y + 10):
			return True
	elif direction == 'left':
		if (snack.x - 10 < snake[-1][0] < snack.x + 10) and (snack.y - 10 < snake[-1][1] + 5 < snack.y + 10):
			return True
	return False

def wall_collision(x, y):
	# makes it so you don't lose multiple lines if you hit the left wall
	if x < 0:
		global direction
		direction = 'right'
		return True
	elif x > 390 or y < 0 or y > 290:
		return True
	return False

def draw_snake(snake):
	for y in snake:
		pygame.draw.rect(canvas, blue, (y[0], y[1], 10, 10))
	return snake




font = pygame.font.SysFont('arial', 20)
food = Food(random.randint(1,400), random.randint(1, 300))
food.draw_food()

while True:
	food.draw_food()

	lives_surface = font.render('Lives: {}'.format(lives), True, green)
	lives_rect = lives_surface.get_rect()
	lives_rect.center = (34, 35)

	score_surface = font.render('Score: {}'.format(score), True, black)
	score_rect = score_surface.get_rect()

	canvas.blit(lives_surface, lives_rect)
	canvas.blit(score_surface, score_rect)

	if direction == 'right':
		snake_body.append(snake_body.pop(0))
		snake_body[-1][0] = snake_body[-2][0] + 10
		snake_body[-1][1] = snake_body[-2][1]
		draw_snake(snake_body)

	if direction == 'left':
		snake_body.append(snake_body.pop(0))
		snake_body[-1][0] = snake_body[-2][0] - 10
		snake_body[-1][1] = snake_body[-2][1]
		draw_snake(snake_body)

	if direction == 'down':
		snake_body.append(snake_body.pop(0))
		snake_body[-1][1] = snake_body[-2][1] + 10
		snake_body[-1][0] = snake_body[-2][0]
		draw_snake(snake_body)

	if direction == 'up':
		snake_body.append(snake_body.pop(0))
		snake_body[-1][1] = snake_body[-2][1] - 10
		snake_body[-1][0] = snake_body[-2][0]
		draw_snake(snake_body)
	
	if food_collision(snake_body, food) == True:
		del food
		food = Food(random.randint(1,400), random.randint(1, 300))
		score += 1
		snake_body.insert(0, [snake_body[0][0] - 10, snake_body[0][1]])
		FPS += 1
	
	if wall_collision(snake_body[-1][0], snake_body[-1][1]) == True or (snake_body[-1] in snake_body[:-1]): #or [snake_body[-1][0], snake_body[-1][1]] in snake_body:
		lives -= 1
		
		if lives == 0:
			break
		snake_body = [[180, 150], [190, 150], [200, 150]]
		FPS = 10
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and direction != 'right':
				direction = 'left'
			elif event.key == pygame.K_RIGHT and direction != 'left' :
				direction = 'right'
			elif event.key == pygame.K_DOWN and direction != 'up':
				direction = 'down'
			elif event.key == pygame.K_UP and direction != 'down':
				direction = 'up'
	
	pygame.display.update()
	fps_clock.tick(FPS)
	canvas.fill(white)

# quits the game if you die
pygame.quit()



