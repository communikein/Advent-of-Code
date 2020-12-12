import math

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

TOP_RIGHT = 0
BOTTOM_RIGHT = 1
BOTTOM_LEFT = 2
TOP_LEFT = 3


MOVE_WAYPOINT = ['N', 'E', 'S', 'W']
TURN_WAYPOINT_LEFT = 'L'
TURN_WAYPOINT_RIGHT = 'R'

MOVE_SHIP_FORWARD = 'F'

SHIP_STARTING_COORDS = [0, 0]
WAYPOINT_STARTING_COORDS = [SHIP_STARTING_COORDS[0] + 10, SHIP_STARTING_COORDS[1] + 1]

COORDS_X = 0
COORDS_Y = 1

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def get_commands(data):
	result = []
	
	for line in data:
		result.append({'cmd': line[0], 'arg': int(line[1:])})

	return result

def move_ship_towards_waypoint(waypoint, ship, value):
	
	ship[COORDS_Y] += value * waypoint[COORDS_Y]
	ship[COORDS_X] += value * waypoint[COORDS_X]

	if debug:
		print(f'Moving ship by {value * waypoint[COORDS_X]} horizontally')
		print(f'Moving ship by {value * waypoint[COORDS_Y]} vertically')

	return ship

def waypoint_in_quadrant(waypoint):
	if waypoint[COORDS_X] > 0 and waypoint[COORDS_Y] > 0:
		return TOP_RIGHT
	if waypoint[COORDS_X] > 0 and waypoint[COORDS_Y] < 0:
		return BOTTOM_RIGHT
	if waypoint[COORDS_X] < 0 and waypoint[COORDS_Y] < 0:
		return BOTTOM_LEFT
	if waypoint[COORDS_X] < 0 and waypoint[COORDS_Y] > 0:
		return TOP_LEFT

def execute_command(ship, waypoint, command):

	# Move waypoint
	if command['cmd'] == MOVE_WAYPOINT[EAST]:
		waypoint[COORDS_X] += command['arg']
	if command['cmd'] == MOVE_WAYPOINT[WEST]:
		waypoint[COORDS_X] -= command['arg']
	if command['cmd'] == MOVE_WAYPOINT[NORTH]:
		waypoint[COORDS_Y] += command['arg']
	if command['cmd'] == MOVE_WAYPOINT[SOUTH]:
		waypoint[COORDS_Y] -= command['arg']

	# Rotate the waypoint around the ship
	if command['cmd'] == TURN_WAYPOINT_LEFT or command['cmd'] == TURN_WAYPOINT_RIGHT:
		waypoint_x = waypoint[COORDS_X]
		waypoint_y = waypoint[COORDS_Y]

		# If rotation by 90
		if command['arg'] == 90:

			temp = waypoint_x
			waypoint_x = waypoint_y
			waypoint_y = temp

			if command['cmd'] == TURN_WAYPOINT_RIGHT:
				waypoint_y = -waypoint_y

			else:
				waypoint_x = -waypoint_x

		elif command['arg'] == 270:

			temp = waypoint_x
			waypoint_x = waypoint_y
			waypoint_y = temp

			if command['cmd'] == TURN_WAYPOINT_RIGHT:
				waypoint_x = -waypoint_x

			else:
				waypoint_y = -waypoint_y

		# If rotation by 180 degrees
		else:
			waypoint_x = -waypoint_x
			waypoint_y = -waypoint_y

		waypoint[COORDS_X] = waypoint_x
		waypoint[COORDS_Y] = waypoint_y
		

	# Move the ship towards the waypoint
	if command['cmd'] == MOVE_SHIP_FORWARD:
		ship = move_ship_towards_waypoint(waypoint, ship, command['arg'])

	return ship, waypoint

global debug
debug = True

input_data = read_input_data('../input.txt')
commands = get_commands(input_data)

ship = SHIP_STARTING_COORDS
waypoint = WAYPOINT_STARTING_COORDS

if debug:
	print(f'Ship status: {ship}')
	print(f'Waypoint status: {waypoint}\n')

for command in commands:
	
	if debug:
		print(f'Command: {command}')

	ship, waypoint = execute_command(ship, waypoint, command)

	if debug:
		print(f'Ship status: {ship}')
		print(f'Waypoint status: {waypoint}\n')

print(ship)
print(abs(ship[0]) + abs(ship[1]))