def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return [int(item) for item in result]

global debug
debug = True

input_data = read_input_data('../input.txt')

def part_1(data):

	prev_read = data[0]
	count_increased = 0
	for line in data[1:]:
		
		if line > prev_read:
			count_increased += 1

		prev_read = line

	return count_increased

part_1_result = part_1(input_data)
print(f'----------------------------------')
print(f'Part 1 result: {part_1_result}\n\n')


def part_2(data, window_size):
	count = [sum(data[i:i+window_size]) for i in range(len(data)-window_size+1)]

	return part_1(count)

part_2_result = part_2(input_data, 3)
print(f'----------------------------------')
print(f'Part 2 result: {part_2_result}\n\n')