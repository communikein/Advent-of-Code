def read_input_data(file):
	input_file = open(file, 'r') 
	input_data = input_file.readlines()
	
	result = []
	for line in input_data:
		line = line.strip()
		result.append(line)

	return result

def format_data(input_data):
	group_data = set()
	result = []
	for line in input_data:
		
		if line == '':
			print('Completed current group, it contains', len(group_data), 'elements')
			result.append(len(group_data))
			group_data.clear()
			print('Started new group..')
			
		else:
			print('Current group is:', group_data)
			group_data.update(list(line))
			print('Added', list(line), 'to current group')
			print('Current group is:', group_data)

		print()

	return result

input_data = read_input_data('input.txt')
formatted_data = format_data(input_data)

print(sum(formatted_data))