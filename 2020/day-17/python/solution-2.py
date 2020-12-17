import itertools

CUBE_INACTIVE = '.'
CUBE_ACTIVE = '#'

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return [[[[state for state in line] for line in result]]]

# TODO: Update to check also neighobrs in the Z dimension
def check_neighbors(cell, space, dims):
	for c in itertools.product(*(range(n-1, n+2) for n in cell)):
		if c != cell and all(0 <= n < dims[i] for i, n in enumerate(c)):
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
	cell_w = cell[3]

	return data[cell_w][cell_z][cell_y][cell_x]


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

# Add one space of CUBE_INACTIVE before the first space in the 4th dimension and after the last
def expand_fourth(data):
	depth = len(data[0])
	height = len(data[0][0])
	width = len(data[0][0][0])
	placeholder_space = [[[CUBE_INACTIVE for _ in range(width)] for _ in range(height)] for _ in range(depth)]

	data.insert(0, placeholder_space)
	data.append(placeholder_space)

	return data

# Add one plane of CUBE_INACTIVE before the first plane in the space and after the last
def expand_space(data):
	height = len(data[0])
	width = len(data[0][0])
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
def update_4d_model(fourth_dimension):

	temp_fourth = []

	for space in fourth_dimension:

		temp_space = []

		for plane in space:

			temp_plane = []

			for row in plane:

				expanded_row = expand_row(row)
				temp_plane.append(expanded_row)

			expanded_plane = expand_plane(temp_plane)		
			temp_space.append(expanded_plane)

		expanded_space = expand_space(temp_space)
		temp_fourth.append(expanded_space)

	return expand_fourth(temp_fourth)



global debug
debug = False

new_data = read_input_data('../input.txt')

cont = 0
for i in range(6):

	# Update 4D model with margins
	data = update_4d_model(new_data)
	new_data = []

	w_size = len(data)
	z_size = len(data[0])
	y_size = len(data[0][0])
	x_size = len(data[0][0][0])

	for w_index in range(w_size):

		new_z_dim = []
		for z_index in range(z_size):

			new_y_dim = []
			for y_index in range(y_size):

				new_x_dim = []
				for x_index in range(x_size):

					cell = (x_index, y_index, z_index, w_index)
					dims = (x_size, y_size, z_size, w_size)

					cell_value = get_cell_value(data, cell)

					neighbors = dict(check_neighbors(cell, data, dims))
					count, active_neighbors = count_active_neighbors(neighbors)
					
					new_cell_value = take_action(cell_value, count)
					new_x_dim.append(new_cell_value)

					if i == 5 and new_cell_value == CUBE_ACTIVE:
						cont += 1

				new_y_dim.append(new_x_dim)

			new_z_dim.append(new_y_dim)

		new_data.append(new_z_dim)

print(cont)