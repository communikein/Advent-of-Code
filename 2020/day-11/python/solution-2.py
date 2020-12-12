EMPTY_SEAT = 'L'
FLOOR = '.'
OCCUPIED_SEAT = '#'

DIRECTION_UP = ('UP', 0)
DIRECTION_DOWN = ('DOWN', 1)
DIRECTION_LEFT = ('LEFT', 2)
DIRECTION_RIGHT = ('RIGHT', 3)
DIRECTION_UP_RIGHT = ('UP-RIGHT', 4)
DIRECTION_UP_LEFT = ('UP-LEFT', 5)
DIRECTION_DOWN_RIGHT = ('DOWN-RIGHT', 6)
DIRECTION_DOWN_LEFT = ('DOWN-LEFT', 7)


def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def count_occupied(data, to_check):
	cont = 0

	seats_value = []
	for coords in to_check:
		check_x = coords[0]
		check_y = coords[1]

		#print(f'Checking neighbor ({check_x}, {check_y}) value: {data[check_y][check_x]}')
		seats_value.append(data[check_y][check_x])

		if data[check_y][check_x] == OCCUPIED_SEAT:
			cont += 1

	#print(seats_value)

	return cont

def check_direction(data, pos_x, pos_y, direction, result=[]):
	move_x = move_y = 0
	map_height = len(data)
	map_width = len(data[0])

	# check requested direction
	if direction[0] == DIRECTION_UP[0] and pos_y > 0:
		move_y = -1
	elif direction[0] == DIRECTION_DOWN[0] and pos_y < map_height - 1:
		move_y = +1
	elif direction[0] == DIRECTION_LEFT[0] and pos_x > 0:
		move_x = -1
	elif direction[0] == DIRECTION_RIGHT[0] and pos_x < map_width - 1:
		move_x = +1
	elif direction[0] == DIRECTION_UP_RIGHT[0] and pos_x < map_width - 1 and pos_y > 0:
		move_x = +1
		move_y = -1
	elif direction[0] == DIRECTION_UP_LEFT[0] and pos_x > 0 and pos_y > 0:
		move_x = -1
		move_y = -1
	elif direction[0] == DIRECTION_DOWN_RIGHT[0] and pos_x < map_width - 1 and pos_y < map_height - 1:
		move_x = +1
		move_y = +1
	elif direction[0] == DIRECTION_DOWN_LEFT[0] and pos_x > 0 and pos_y < map_height - 1:
		move_x = -1
		move_y = +1

	# If I completed this direction without finding any seat
	if move_x == 0 and move_y == 0:
		result[direction[1]] = None
		return

	# Check new position
	pos_x += move_x
	pos_y += move_y
	seat_value = data[pos_y][pos_x]

	# If it's floor, keep on looking
	if seat_value == FLOOR:
		check_direction(data, pos_x, pos_y, direction, result)

	# If it's a seat, terminate and return seat value
	else:
		result[direction[1]] = seat_value

def seat_action(data, seat_x, seat_y):
	global debug

	if debug:
		print(f'\nAnalysing seat ({seat_x}, {seat_y})')

	seats_seens = [None for i in range(8)]
	if debug:
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_UP, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_UP[0]}, found {seats_seens[DIRECTION_UP[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_DOWN, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_DOWN[0]}, found {seats_seens[DIRECTION_DOWN[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_LEFT, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_LEFT[0]}, found {seats_seens[DIRECTION_LEFT[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_RIGHT, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_RIGHT[0]}, found {seats_seens[DIRECTION_RIGHT[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_UP_RIGHT, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_UP_RIGHT[0]}, found {seats_seens[DIRECTION_UP_RIGHT[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_UP_LEFT, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_UP_LEFT[0]}, found {seats_seens[DIRECTION_UP_LEFT[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_DOWN_RIGHT, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_DOWN_RIGHT[0]}, found {seats_seens[DIRECTION_DOWN_RIGHT[1]]}')
		print(seats_seens)

	check_direction(data, seat_x, seat_y, DIRECTION_DOWN_LEFT, seats_seens)
	if debug:
		print(f'Direction {DIRECTION_DOWN_LEFT[0]}, found {seats_seens[DIRECTION_DOWN_LEFT[1]]}')
		print(seats_seens)

	count = seats_seens.count(OCCUPIED_SEAT)

	seat_value = data[seat_y][seat_x]
	changes = 0
	if data[seat_y][seat_x] == EMPTY_SEAT and count == 0:
		changes = 1
		seat_value = OCCUPIED_SEAT
	if data[seat_y][seat_x] == OCCUPIED_SEAT and count >= 5:
		changes = 1
		seat_value = EMPTY_SEAT

	return changes, seat_value


input_data = read_input_data('../input.txt')

global debug
debug = False
changes = 1
occupied_seats = 0
cont = 0
while changes > 0:
	
	occupied_seats = 0
	changes = 0

	# Create empty copy of input_data
	working_data = [['.' for i in input_data[0]] for x in input_data]

	for seat_y in range(len(input_data)):
		for seat_x in range(len(input_data[0])):
			
			seat_current_value = input_data[seat_y][seat_x]

			# Floor doesn't change
			if seat_current_value == '.':
				continue

			# 
			changed, value = seat_action(input_data, seat_x, seat_y)
			if debug and changed > 0:
				print(f'Seat changed to {value}')
			changes += changed

			#print(f'({seat_x}, {seat_y})')
			working_data[seat_y][seat_x] = value
			if value == OCCUPIED_SEAT:
				occupied_seats += 1


	input_data = working_data

	if debug:
		print()
		for i in working_data:
			print(i)
	print()
	print(occupied_seats)
	
	if cont > 9999999:
		break

	cont += 1
