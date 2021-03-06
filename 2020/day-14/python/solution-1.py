import re


def read_input_data(file):
	with open(file, 'r') as input_file:
		temp = input_file.read()

	matches = re.findall('(mask = (\w*))?(mem\[(\d*)\] = (\d*))?\n', temp)
	
	# Create a dictionary of all the 'mask = xxxxxxxxxxxxxxxxxxxxx' operations	
	result_masks = {index: {'mask': op[1]} for index, op in enumerate(matches) if op[0] != ''}

	# Create a dictionary of all the 'mem[x] = y' operations
	result_mems = {index: {'mem_index': int(op[3]), 'mem_val': f'{int(op[4]):036b}'} for index, op in enumerate(matches) if op[0] == ''}

	# Join the two dictionaries
	result = {**result_masks, **result_mems}

	return result

def apply_mask(mask, data):
	
	result = [mask[i] if mask[i] != 'X' else data[i] for i in range(len(mask))]

	return ''.join(result)


input_data = read_input_data('../input.txt')

data = {}
mask = ''
for op_index in sorted(input_data):

	if 'mask' in input_data[op_index]:
		mask = input_data[op_index]['mask']

	else:
		mem_val = input_data[op_index]['mem_val']
		mem_index = input_data[op_index]['mem_index']

		val = apply_mask(mask, mem_val)
		data[mem_index] = int(val, 2)

print(sum(data.values()))