#Snakegame Jesper-Andersson

# TODO:
# Background keyboard input
# Apples & point display
# "Snake" part

import time
from os import system, name

snake = "+"
background = "-"
apple = "O"

grid = [background, background, background,
		background, snake, background,
		background, background, background]

old_pos = 0
snake_position = 4
grid_width = 3

def draw_grid():
	i = 0
	while i < 9:
		print(grid[i], end='')
		i += 1
		if i % grid_width == 0:
			print('\n')

def move_up(snake_position, grid_width, old_pos):
	old_pos = snake_position
	snake_position = snake_position - grid_width
def move_down(snake_position, grid_width, old_pos):
	old_pos = snake_position
	snake_position = snake_position + grid_width
def move_left(snake_position, old_pos):
	old_pos = snake_position
	snake_position = snake_position - 1
def move_right(snake_position, old_pos):
	old_pos = snake_position
	snake_position = snake_position + 1

def scoreboard():
	pass

def update_movement(snake_position, old_pos, grid, snake, background):
	grid[snake_position] = snake
	grid[old_pos] = background
	clear()
	draw_grid()

def clear(): 
    _ = system('cls')

#Frontend stuff

clear()
draw_grid()
time.sleep(5)
clear()
time.sleep(5)