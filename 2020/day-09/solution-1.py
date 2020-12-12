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


input_data = read_input_data('input.txt')

cont = 0
while cont < len(input_data):
	print(cont)
	current = cont + PREAMBLE_LEN
	print(current)
	preamble = input_data[cont:current]
	print(preamble)
	sum_combos = sum_combinations(preamble)
	print(sum_combos)
	
	if int(input_data[current]) not in sum_combos:
		print(input_data[current])
		print(current)
		break

	cont += 1