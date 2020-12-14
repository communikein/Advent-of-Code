'''
solution example: 1068781
'''


def read_input_data(file):
	with open(file, 'r') as input_file:
		temp = input_file.read()

	# Split by '\n' or ','
	result = temp.replace('\n', ' ').replace(',', ' ').split()
	
	# Convert numbers to int and remove first line
	result = ["x" if x == "x" else int(x) for x in result[1:]]

	final = {bus: -index % bus for index, bus in enumerate(result) if bus != "x"}

	return final


global debug
debug = False

input_data = read_input_data('../input.txt')

bus_ids = list(sorted(input_data, reverse = True))
if debug:
	print(f'bus_ids: {bus_ids}')

timestamp = input_data[bus_ids[0]]
if debug:
	print(f'timestamp: {timestamp}')

previous_bus_id_rtt = bus_ids[0]
if debug:
	print(f'previous_bus_id_rtt: {previous_bus_id_rtt}')

# For each bus in descending order
for current_bus_id_rtt in bus_ids[1:]:
	if debug:
		print(f'current_bus_id_rtt: {current_bus_id_rtt}')
	
	# So long as bus_id didn't pass with the correct difference
	while timestamp % current_bus_id_rtt != input_data[current_bus_id_rtt]:
		if debug:
			print(f'timestamp % current_bus_id_rtt != input_data[current_bus_id_rtt]')
			print(f'{timestamp} % {current_bus_id_rtt} = {timestamp%current_bus_id_rtt}')
		
		# Increase timestamp by the previous bus (the one just greater) rtt
		timestamp += previous_bus_id_rtt
		if debug:
			print(f'timestamp {timestamp}')


	previous_bus_id_rtt *= current_bus_id_rtt
	if debug:
		print(f'previous_bus_id_rtt = previous_bus_id_rtt * current_bus_id_rtt -> {previous_bus_id_rtt}')

print(f'timestamp {timestamp}')