import itertools

PREAMBLE_LEN = 25

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result


def sum_combinations(previous_25):
	combos = itertools.combinations(previous_25, 2)

	result = []
	for combo in combos:
		result.append(int(combo[0]) + int(combo[1]))

	return result

def find_off_number(input_data):
	cont = 0
	while cont < len(input_data):
		current = cont + PREAMBLE_LEN
		preamble = input_data[cont:current]
		sum_combos = sum_combinations(preamble)
		
		if int(input_data[current]) not in sum_combos:
			return int(input_data[current])

		cont += 1

def compute_kwindows(input_data, k):
	pointer


input_data = read_input_data('../input.txt')
off_number = find_off_number(input_data)

list_to_sum = []
pointer = 0
window_head = 0
while pointer < len(input_data):
	num = int(input_data[pointer])
	temp_sum = sum(list_to_sum) + num
	
	if temp_sum < off_number:
		list_to_sum.append(num)
		pointer += 1
	
	elif temp_sum == off_number:
		list_to_sum.append(num)
		max_num = max(list_to_sum)
		min_num = min(list_to_sum)
		sum_num = max_num + min_num
		print(f'Min: {min_num} -- Max: {max_num} -- Sum: {sum_num}' )
		break

	else:
		list_to_sum.clear()
		window_head += 1
		pointer = window_head