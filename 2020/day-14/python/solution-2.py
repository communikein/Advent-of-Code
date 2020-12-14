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

def apply_mask_to_address(address, mask):
	
	result = ['']
	index = 0
	while index < len(mask):

		if mask[index] == '0':

			result = [addr + address[index] for addr in result]
		
		elif mask[index] == '1':

			result = [addr + mask[index] for addr in result]

		else:

			result_0 = [addr + '0' for addr in result]
			result_1 = [addr + '1' for addr in result]
			result = result_0 + result_1

		index += 1
	
	return result


input_data = read_input_data('../input.txt')

data = {}
mask = ''
for op_index in sorted(input_data):

	if 'mask' in input_data[op_index]:
		
		mask = input_data[op_index]['mask']

	else:
		mem_val = input_data[op_index]['mem_val']
		mem_addr = input_data[op_index]['mem_index']

		new_addresses = apply_mask_to_address(f'{mem_addr:036b}', mask)

		for addr in new_addresses:
			data[int(addr, 2)] = int(mem_val, 2)

print(sum(data.values()))