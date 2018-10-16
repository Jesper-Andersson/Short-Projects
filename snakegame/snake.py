#Snakegame Jesper-Andersson

# TODO:
# Background keyboard input DONE
# Remove empty line between grid rows DONE
# Impassable borders KINDA DONE
# User defined grid size DONE
# Apples & point display DONE
# Border Generation
# Game over
# "Snake" part (Automatic movement, tail growing)

import time
import math
import random
from os import system, name
import keyboard

snake = "S"
background = " "
border = "!"
apple = "O"
runnable = False

def clear(): 
    _ = system('cls')

while runnable == False:
	print("16, 25, 36, 49, 64, 81, 100")
	gridsize = int(input("Skriv in önskad storlek på spelytan: "))
	if gridsize in {16, 25, 36, 49, 64, 81, 100}:
		runnable = True
	else: 
		clear()
		print("Ogiltid spelyta storlek")

grid = [background] * gridsize 
grid_width = int(math.sqrt(len(grid)))

def border_creator():
	pass

running = True
snake_position = 5
total_score = 0
score_worth = 1
apple_pos = 0

def draw_grid():
	clear()
	scoreboard()
	i = 0
	while i < len(grid):
		print(grid[i], end='')
		i += 1
		if i % grid_width == 0:
			print('')

def update_movement(old_pos):
	global grid
	global snake_position
	grid[snake_position] = snake
	grid[old_pos] = background
	draw_grid()
	
def snake_spawner():
	global snake_position
	snake_position = random.randint(0, len(grid))
	grid[snake_position] = snake

def apple_spawner():
	global apple_pos
	apple_pos = random.randint(0, len(grid))
	grid[apple_pos] = apple

#up_calc = snake_position - grid_width
def move_up():
	global snake_position
	if snake_position - grid_width >= 0 and snake_position - grid_width < gridsize:
		if grid[snake_position - grid_width] != border:
			old_pos = snake_position
			snake_position = snake_position - grid_width
			if grid[snake_position] == apple:
				add_score()
			update_movement(old_pos)
	else: pass

#down_calc = snake_position + grid_width
def move_down():
	global snake_position
	if snake_position + grid_width >= 0 and snake_position + grid_width < gridsize:
		if grid[snake_position + grid_width] != border:
			old_pos = snake_position
			snake_position = snake_position + grid_width
			if grid[snake_position] == apple:
				add_score()
			update_movement(old_pos)
	else: pass

#left_calc = snake_position - 1
def move_left():
	global snake_position
	if snake_position - 1 >= 0 and snake_position - 1 < gridsize:
		if grid[snake_position - 1] != border:
			old_pos = snake_position
			snake_position = snake_position - 1
			if grid[snake_position] == apple:
				add_score()
			update_movement(old_pos)
	else: pass

#right_calc = snake_position + 1
def move_right():
	global snake_position
	if snake_position + 1 >= 0 and snake_position + 1 < gridsize:
		if grid[snake_position + 1] != border:
			old_pos = snake_position
			snake_position = snake_position + 1
			if grid[snake_position] == apple:
				add_score()
			update_movement(old_pos)
	else: pass

def scoreboard():
	global total_score
	print('Your score is: ' + str(total_score))

def add_score():
	global score_worth
	global total_score
	total_score += score_worth
	apple_spawner()

snake_spawner()
apple_spawner()
draw_grid()
if runnable == True:
	while running == True:
		if keyboard.is_pressed('w') == True:
			move_up()
			time.sleep(0.2)
		if keyboard.is_pressed('a') == True:
			move_left()
			time.sleep(0.2)
		if keyboard.is_pressed('s') == True:
			move_down()
			time.sleep(0.2)
		if keyboard.is_pressed('d') == True:
			move_right()
			time.sleep(0.2)