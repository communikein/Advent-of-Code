EMPTY_SEAT = 'L'
FLOOR = '.'
OCCUPIED_SEAT = '#'

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

def seat_action(data, seat_x, seat_y):

	# If seat in first row
	if seat_y == 0:
		
		# If seat in first column
		if seat_x == 0:
			to_check = [(seat_x+1, seat_y), (seat_x, seat_y+1), (seat_x+1, seat_y+1)]

		# If seat in last column
		elif seat_x == len(data[0]) - 1:
			to_check = [(seat_x-1, seat_y), (seat_x, seat_y+1), (seat_x-1, seat_y+1)]

		# If seat somewhere in the middle
		else:
			to_check = [
				(seat_x+1, seat_y), (seat_x, seat_y+1), (seat_x+1, seat_y+1),
				(seat_x-1, seat_y), (seat_x-1, seat_y+1)]

	# If seat in last row
	elif seat_y == (len(data) - 1):

		# If seat in first column
		if seat_x == 0:
			to_check = [(seat_x+1, seat_y), (seat_x, seat_y-1), (seat_x+1, seat_y-1)]

		# If seat in last row
		elif seat_x == len(data[0]) - 1:
			to_check = [(seat_x-1, seat_y), (seat_x, seat_y-1), (seat_x-1, seat_y-1)]

		# If seat somewhere in the middle
		else:
			to_check = [
				(seat_x+1, seat_y), (seat_x, seat_y-1), (seat_x+1, seat_y-1),
				(seat_x-1, seat_y), (seat_x-1, seat_y-1)]

	# If seat somewhere in the middle
	else:

		# If seat in first column
		if seat_x == 0:
			to_check = [
				(seat_x+1, seat_y), (seat_x, seat_y-1), (seat_x+1, seat_y-1),
				(seat_x, seat_y+1), (seat_x+1, seat_y+1)]

		# If seat in last row
		elif seat_x == len(data[0]) - 1:
			to_check = [
				(seat_x-1, seat_y), (seat_x, seat_y-1), (seat_x-1, seat_y-1),
				(seat_x, seat_y+1), (seat_x-1, seat_y+1)]

		# If seat somewhere in the middle
		else:
			to_check = [
				(seat_x-1, seat_y-1), (seat_x, seat_y-1), (seat_x+1, seat_y-1),
				(seat_x-1, seat_y), (seat_x+1, seat_y), 
				(seat_x-1, seat_y+1),(seat_x, seat_y+1),(seat_x+1, seat_y+1),]

	count = count_occupied(data, to_check)

	seat_value = data[seat_y][seat_x]
	changes = 0
	if data[seat_y][seat_x] == 'L' and count == 0:
		changes = 1
		seat_value = '#'
	if data[seat_y][seat_x] == '#' and count >= 4:
		changes = 1
		seat_value = 'L'

	return changes, seat_value


input_data = read_input_data('input.txt')

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

		#	print(f'\nAnalysing ({seat_x}, {seat_y}) -- {seat_current_value}')

			# 
			changed, value = seat_action(input_data, seat_x, seat_y)
			changes += changed

			print(f'{len(input_data)} -- ({seat_x}, {seat_y})')
			working_data[seat_y][seat_x] = value
			if value == OCCUPIED_SEAT:
				occupied_seats += 1


	input_data = working_data

	#print()
	for i in working_data:
		print(i)
	print(occupied_seats)
	print()

	if cont > 999999:
		break

	cont += 1
