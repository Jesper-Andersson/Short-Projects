#Snakegame Jesper-Andersson

# TODO:
# Background keyboard input
# Unpassable borders
# Game over
# Apples & point display
# "Snake" part
# Remove empty line between grid rows

import time
import math
from os import system, name
import keyboard

snake = "+"
background = "-"
apple = "O"

grid = [background, background, background, background,
		background, snake, 		background, background,
		background, background, background, background,
		background, background, background, background
		]

snake_position = 4
total_score = 0
score_worth = 1

grid_width = int(math.sqrt(len(grid)))
print(str(grid_width))

def clear(): 
    _ = system('cls')

def draw_grid():
	clear()
	scoreboard()
	i = 0
	while i < len(grid):
		print(grid[i], end='')
		i += 1
		if i % grid_width == 0:
			print('\n')

def update_movement(old_pos):
	global grid
	global snake_position

	grid[snake_position] = snake
	grid[old_pos] = background
	draw_grid()

def move_up():
	global snake_position

	old_pos = snake_position
	snake_position = snake_position - grid_width
	update_movement(old_pos)

def move_down():
	global snake_position

	old_pos = snake_position
	snake_position = snake_position + grid_width
	update_movement(old_pos)

def move_left():
	global snake_position

	old_pos = snake_position
	snake_position = snake_position - 1
	update_movement(old_pos)

def move_right():
	global snake_position

	old_pos = snake_position
	snake_position = snake_position + 1
	update_movement(old_pos)

def scoreboard():
	global total_score
	print('Your score is: ' + str(total_score))

def addscore():
	global score_worth
	global total_score
	total_score += score_worth

draw_grid()

keyboard.add_hotkey('w', move_up())
keyboard.add_hotkey('a', move_left())
keyboard.add_hotkey('s', move_down())
keyboard.add_hotkey('d', move_right())

move_right()
move_right()