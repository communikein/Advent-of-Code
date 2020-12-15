from datetime import datetime 


def read_input_data(file):

	return {int(num): index+1 for index, num in enumerate(file.split(','))}

def find_next_number(data, prev_numbers, last_number, current_count):

	if last_number in prev_numbers:
		if debug:
			print(f'ALREADY PRESENT - {last_number}')
			print(f'Current count: {current_count}, Last count: {data[last_number]}')
			print(f'New number: {current_count - data[last_number]}')
		return current_count - data[last_number]

	else:
		if debug:
			print(f'NEW FOUND - {last_number}')
			print(f'New number: 0')

		return 0


global debug
debug = False

input_data = '2,15,0,9,1,20'
#input_data = '0,3,6'

data = read_input_data(input_data)
if debug:
	print(data)

new_number = 0
last_number = None
starting_time = datetime.now()
print(starting_time)

prev_numbers = set()

y = 0
for y in range(30000000):

	if y < len(data):

		if last_number != None:
			prev_numbers.add(last_number)

		if debug:
			print(f'SKIPPING: {last_number}')

		last_number = list(data.keys())[y]
		
		if debug:
			print(f'NEW LAST NUMBER: {last_number}')
			print(f'prev numbers: {prev_numbers}')
		
		continue

	else:

		if debug:
			print(f'Analysing: {last_number}')
		
		# Compute new number
		new_number = find_next_number(data, prev_numbers, last_number, y)

		# Add last number to previous numbers
		prev_numbers.add(last_number)
		data[last_number] = y
		if debug:
			print(f'Prev numbers: {prev_numbers}')
			print(f'Data: {data}')
		
		# Update data with current counter for the new number found
		#data[new_number] = y + 1
		
		# Update the last number, with the new number found
		last_number = new_number

		if debug:
			print(f'Last number: {last_number}')

	#print(f'{y+1} - {(y+1)/30000000*100:.4f}% - {datetime.now() - starting_time} - {new_number}')

print(f'{y+1} - {(y+1)/30000000*100:.4f}% - {datetime.now() - starting_time} - {new_number}')
