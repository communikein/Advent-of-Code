def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def prepare_data(data):
	temp = [0]
	
	for d in data:
		temp.append(int(d))

	temp.sort()

	return temp

# Return how many following adapters can be used with current
def check_following_adapters(data, pointer=0):
	return [i for i in data[pointer:pointer+4] if ((i - data[pointer]) <= 3 and (i - data[pointer]) > 0)]

def count_subtrees(data, counter=[0], cache={}):
	
	current_adapter = data[0]
	
	# If I already computed this adapter, use cached result
	if current_adapter in cache.keys():
		counter[0] += cache[current_adapter]
	
	else:

		# If last adapter, increase counter by 1
		if len(data) == 1:
			counter[0] += 1
			
		# If not last adapter, compute following adapters
		else:
			forks = check_following_adapters(data)

			offset = 1
			while offset <= len(forks):
				count_subtrees(data[offset:], counter, cache)
				offset += 1

		# Cache result
		cache[current_adapter] = counter[0]


input_data = read_input_data('input.txt')
ordered_data = prepare_data(input_data)

counter = [0]
count_subtrees(ordered_data, counter)
print(counter)