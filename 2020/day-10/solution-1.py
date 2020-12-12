import itertools

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def format_data(data):
	temp = [0]
	
	for d in data:
		temp.append(int(d))

	temp.sort()
	temp.append(temp[-1]+3)

	result = []
	i = 0
	while i < len(temp) - 1:
		result.append(temp[i+1] - temp[i])
		i += 1

	return result


input_data = read_input_data('input.txt')
ordered_data = format_data(input_data)

one_diff = ordered_data.count(1)
three_diff = ordered_data.count(3)

print(one_diff * three_diff)