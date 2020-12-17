import itertools

CUBE_INACTIVE = '.'
CUBE_ACTIVE = '#'

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return [[[state for state in line] for line in result]]

# TODO: Update to check also neighobrs in the Z dimension
def check_neighbors(cell, space, xy_size, z_size):
	for c in itertools.product(*(range(n-1, n+2) for n in cell)):
		if c != cell and all(0 <= n < xy_size for n in c[:2]) and (0 <= c[2] < z_size):
			yield c, get_cell_value(space, c)

# Return number of CUBE_ACTIVE cells in neighbors, as well as those cells coords
def count_active_neighbors(neighbors):
	result = []
	for neigh in neighbors:
		if neighbors[neigh] == CUBE_ACTIVE:
			result.append(neigh)

	return len(result), result

def get_cell_value(data, cell):
	cell_x = cell[0]
	cell_y = cell[1]
	cell_z = cell[2]

	return data[cell_z][cell_y][cell_x]


# Choose whether to change current cell status or not
def take_action(cell_value, active_neighbors):
	
	if cell_value == CUBE_ACTIVE:
	
		if active_neighbors == 2 or active_neighbors == 3:
			return CUBE_ACTIVE
		else:
			return CUBE_INACTIVE
	
	else:

		if active_neighbors == 3:
			return CUBE_ACTIVE
		else:
			return CUBE_INACTIVE

# Add one plane of CUBE_INACTIVE before the first plane in the space and after the last
def expand_space(data):
	width = len(data[0])
	height = len(data[0][0])
	placeholder_plane = [[CUBE_INACTIVE for _ in range(width)] for _ in range(height)]

	data.insert(0, placeholder_plane)
	data.append(placeholder_plane)

	return data

# Add one row of CUBE_INACTIVE before the first row in the plane and after the last
def expand_plane(data):
	width = len(data[0])
	placeholder_plane = [CUBE_INACTIVE for _ in range(width)]

	data.insert(0, placeholder_plane)
	data.append(placeholder_plane)

	return data

# Add one CUBE_INACTIVE before the first cell in the row and after the last
def expand_row(data):

	data.insert(0, CUBE_INACTIVE)
	data.append(CUBE_INACTIVE)

	return data

# Add one layer of CUBE_INACTIVE around the current 3D space
def update_3d_model(space):

	temp_space = []

	for plane in space:

		temp_plane = []

		for row in plane:
			temp_plane.append(expand_row(row))

		temp_space.append(expand_plane(temp_plane))

	return expand_space(temp_space)


new_data = read_input_data('../input.txt')

for i in range(6):

	# Update 3D model with padding
	data = update_3d_model(new_data)
	new_data = []

	z_size = len(data)
	y_size = len(data[0])
	x_size = len(data[0][0])

	for z_index in range(z_size):

		new_y_dim = []
		for y_index in range(y_size):

			new_x_dim = []
			for x_index in range(x_size):

				cell = (x_index, y_index, z_index)
				cell_value = get_cell_value(data, cell)

				neighbors = dict(check_neighbors(cell, data, len(data[z_index]), len(data)))
				count, active_neighbors = count_active_neighbors(neighbors)
				
				new_cell_value = take_action(cell_value, count)
				new_x_dim.append(new_cell_value)

			new_y_dim.append(new_x_dim)

		new_data.append(new_y_dim)

cont = 0
for z in new_data:
	for y in z:
		for x in y:
			if x == CUBE_ACTIVE:
				cont += 1

print(cont)