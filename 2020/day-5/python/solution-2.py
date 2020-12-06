def read_input_data(file):
	input_file = open(file, 'r') 
	input_data = input_file.readlines()
	
	result = []
	for line in input_data:
		line = line.strip()
		result.append(line)

	return result

def format_input_data(input_data):
	result = []
	for line in input_data:
		seat_row = line[:7].replace('F', '0').replace('B', '1')
		seat_col = line[7:].replace('L', '0').replace('R', '1')

		result.append(seat_row + seat_col)

	result.sort()
	return result

def compute_row(ticket_row):
	binary_value = ticket_row.replace('F', '0').replace('B', '1')
	return int(binary_value, base=2)

def compute_col(ticket_col):
	binary_value = ticket_col.replace('L', '0').replace('R', '1')
	return int(binary_value, base=2)

def compute_seat(row, col):
	seat_id = row * 8 + col
	
	seat = {}
	seat[seat_id] = {'seat_row': row, 'seat_col': col}

	return seat

def find_missing_seat(row, row_seated_seats, all_seats_ids):
	stock_seats = [i for i in range(8)]

	missing_seats = list(set(stock_seats) - set(row_seated_seats))
		
	my_seat = {}
	for seat in missing_seats:
		prev_seat_id = row * 8 + (seat - 1)
		next_seat_id = row * 8 + (seat + 1)

		if prev_seat_id in all_seats_ids and next_seat_id in all_seats_ids:
			my_seat = compute_seat(row, seat)
			
	return my_seat

def find_seats(input_data):
	result = {}

	for seat in input_data:
		current_seat_row = int(seat[:7], base=2)
		current_seat_col = int(seat[7:], base=2)
		current_seat_id = current_seat_row * 8 + current_seat_col
		current_seat = compute_seat(current_seat_row, current_seat_col)

		result[current_seat_id] = current_seat[current_seat_id]

	return result

def find_my_seat(input_data, all_seats_ids):
	my_seat = {}

	previous_seats = {0: []}
	current_seats = {0: []}
	for seat in input_data:
		current_seat_row = int(seat[:7], base=2)
		current_seat_col = int(seat[7:], base=2)
		current_seat_id = current_seat_row * 8 + current_seat_col
		current_seat = compute_seat(current_seat_row, current_seat_col)
		
		if my_seat == {}:
			print('Current row:', current_seat_row)
				
			''' 
			If this is the first seat of a new row:
				- copy current_seats to previous_seats 
				- empty current_seats
			'''
			if current_seat_row != list(current_seats.keys())[0]:
				print('NEW ROW')
				print('Transferring current_seats into previous_seats')
				previous_seats = current_seats
				print('Creating current_seats for row', current_seat_row)
				current_seats = {current_seat_row: []}
				print('Current seats:', current_seats)
				print('Previous seats:', previous_seats)

			print('Added seat', current_seat_col, 'to current row')
			current_seats[current_seat_row].append(current_seat_col)
			print('Current seats:', current_seats)
			
			''' If the previous row is a candidate for my seat, look for it '''
			print('Looking for missing seat')
			print(previous_seats[current_seat_row-1])
			my_seat = find_missing_seat(current_seat_row-1, previous_seats[current_seat_row-1], all_seats_ids)
			print('FOUND MISSING SEAT')
			print(my_seat)
			print()

	return my_seat


input_data = read_input_data('../input.txt')
formatted_data = format_input_data(input_data)
seats = find_seats(formatted_data)
my_seat = find_my_seat(formatted_data, list(seats.keys()))

print('My seat is:', my_seat)