def read_input_data(file):
	input_file = open(file, 'r') 
	input_data = input_file.readlines()
	
	result = []
	for line in input_data:
		line = line.strip()
		result.append(line)

	return result

def format_data(input_data):
	group_answers = set()
	result = []

	first_entries = True
	for line in input_data:
		
		if line == '':
			print('Completed current group, it contains', len(group_answers), 'elements')
			
			result.append(len(group_answers))
			group_answers.clear()
			first_entries = True

			print('Started new group..')
			
		else:
			print('Current group is:', group_answers)
			
			person_answers = set()
			person_answers.update(list(line))
			print('Current person answered', person_answers)
			
			if first_entries:
				group_answers.update(person_answers)
				print('Added to group.')
				first_entries = False
			else:
				common_answers = group_answers.intersection(person_answers)
				group_answers.intersection_update(person_answers)
				print('Common answers:', common_answers)

			print('Current group is:', group_answers)

		print()

	return result

input_data = read_input_data('../input.txt')
formatted_data = format_data(input_data)

print(sum(formatted_data))