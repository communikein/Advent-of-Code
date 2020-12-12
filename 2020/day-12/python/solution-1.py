NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

MOVE = ['N', 'E', 'S', 'W']
MOVE_NORTH = ('N', NORTH)
MOVE_EAST = ('E', EAST)
MOVE_SOUTH = ('S', SOUTH)
MOVE_WEST = ('W', WEST)

TURN_LEFT = 'L'
TURN_RIGHT = 'R'
MOVE_FORWARD = 'F'

SHIP_COORD_X = 0
SHIP_COORD_Y = 1

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def get_commands(data):
	result = []
	
	for line in data:
		result.append({'cmd': line[0], 'arg': int(line[1:])})

	return result

def move_ship(ship, command):
	if command['cmd'] == MOVE[EAST]:
		ship['coords'][SHIP_COORD_X] += command['arg']
	if command['cmd'] == MOVE[WEST]:
		ship['coords'][SHIP_COORD_X] -= command['arg']

	if command['cmd'] == MOVE[NORTH]:
		ship['coords'][SHIP_COORD_Y] -= command['arg']
	if command['cmd'] == MOVE[SOUTH]:
		ship['coords'][SHIP_COORD_Y] += command['arg']

	if command['cmd'] == TURN_LEFT:
		new_direction = (ship['direction'] - command['arg'] / 90) % 4
		ship['direction'] = int(new_direction)
	if command['cmd'] == TURN_RIGHT:
		new_direction = (ship['direction'] + command['arg'] / 90) % 4
		ship['direction'] = int(new_direction)

	if command['cmd'] == MOVE_FORWARD:
		new_command = {'cmd': MOVE[ship['direction']], 'arg': command['arg']}
		ship = move_ship(ship, new_command)

	return ship



input_data = read_input_data('../input.txt')
commands = get_commands(input_data)

ship = {'direction': EAST, 'coords': [0, 0]}


for command in commands:
	ship = move_ship(ship, command)

print(ship)
print(sum(ship['coords']))