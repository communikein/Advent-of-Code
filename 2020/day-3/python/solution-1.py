import itertools
import math

def read_input_data(file):
	input_file = open(file, 'r') 
	input_data = input_file.readlines()
	
	result = []
	for line in input_data:
		result.append(line.strip())

	return result

def fix_map(starting_map):
	starting_height = len(starting_map)
	starting_width = len(starting_map[0])

	final_map = []
	for row in starting_map:
		new_row = row * math.ceil(starting_height / starting_width * 3)
		final_map.append(new_row[:starting_height*3])

	return final_map, starting_height, starting_height

current_x = 0
current_y = 0
move_x = 3
move_y = 1

input_data = read_input_data('input.txt')
map_data, map_height, map_width = fix_map(input_data)

trees = 0
for _ in range(0, map_height):
	if map_data[current_y][current_x] == '#':
		
		trees += 1

	current_y += 1
	current_x += 3

print(trees)