import re

OP_MUL = '*'
OP_ADD = '+'
OP_OPEN_PAR = '('
OP_CLOSE_PAR = ')'


all_elements_rule = '(\d+)|(?: )|(\+)|(\*)|(\()|(\))'

def read_input_data(file):
	with open(file, 'r') as input_file:
		temp = input_file.read().split('\n')
	
	# Gather equations elements
	raw_matches = [re.split(all_elements_rule, line) for line in temp]
	equation_elements = [[el for el in line if el != None and el != ''] for line in raw_matches]

	return equation_elements


def compute_group(elements):
	acc = int(elements[0])

	index = 1
	while index < len(elements):
		
		if elements[index] == OP_ADD:
			acc += int(elements[index+1])

		if elements[index] == OP_MUL:
			acc *= int(elements[index+1])

		index += 1

	return acc

def find_innermost_group(elements):

	index_open_par = 0
	index_close_par = len(elements)

	if OP_OPEN_PAR not in elements:
		return elements, (index_open_par, index_close_par)

	index = 0
	for el in elements:

		if el == OP_OPEN_PAR:
			index_open_par = index

		if el == OP_CLOSE_PAR:
			index_close_par = index
			break

		index += 1

	return elements[index_open_par+1:index_close_par], (index_open_par, index_close_par+1)

def replace_innermost_group_with_result(equation):
	group, indices = find_innermost_group(equation)
	result = compute_group(group)

	del equation[indices[0]:indices[1]]
	equation.insert(indices[0], str(result))

	return equation

def solve_equation(equation):

	step_result = replace_innermost_group_with_result(equation)

	while len(step_result) > 1:
		step_result = replace_innermost_group_with_result(step_result)

	return int(step_result[0])



new_data = read_input_data('../input.txt')

acc = 0
for equation in new_data:
	eq_result = solve_equation(equation)
	acc += eq_result

print(acc)
