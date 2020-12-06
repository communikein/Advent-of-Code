import itertools
import math

'''
64
284
71
68
40

final: 3510149120
'''

current_x = 0
current_y = 0
move_x = 7
move_y = 1

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
	width_mult = math.ceil(starting_height / starting_width * move_x)
	if starting_height > starting_width:
		for row in starting_map:
			new_row = row * width_mult
			final_map.append(new_row[:starting_height * move_x])

		final_width = starting_height * move_x
		final_height = starting_height
	else:
		final_map = starting_map
		final_height, final_width = starting_height, starting_width

	return final_map, final_height, final_width

input_data = read_input_data('../input.txt')
map_data, map_height, map_width = fix_map(input_data)

trees = 0
for _ in range(0, map_height):
	#print(map_height, map_width)
	#print(current_y, current_x)
	if map_data[current_y][current_x] == '#':	
		trees += 1

	current_y += move_y
	current_x += move_x

	if current_y >= map_height or current_x >= map_width:
		break

print(trees)