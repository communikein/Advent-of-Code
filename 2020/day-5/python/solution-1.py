def read_input_data(file):
	input_file = open(file, 'r') 
	input_data = input_file.readlines()
	
	result = []
	for line in input_data:
		line = line.strip()
		result.append(line)

	return result

def compute_row(ticket_row):
	binary_value = ticket_row.replace('F', '0').replace('B', '1')
	return int(binary_value, base=2)

def compute_col(ticket_col):
	binary_value = ticket_col.replace('L', '0').replace('R', '1')
	return int(binary_value, base=2)

def find_seats(input_data):
	result = {}
	for seat in input_data:

		seat_row = compute_row(seat[:7])
		seat_col = compute_col(seat[7:])
		seat_id = seat_row * 8 + seat_col

		result[seat_id] = {'seat_row': seat_row, 'seat_col': seat_col}

	return result

input_data = read_input_data('input.txt')
seats = find_seats(input_data)

print(len(seats))
print(max(seats.keys()))