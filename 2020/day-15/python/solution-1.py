
def read_input_data(file):

	return [int(i) for i in file.split(',')]

def find_next_number(data):
		
	#print(f'Analysing {data[-1]} in {data[:-1]}')

	if data[-1] in data[:-1]:
		
		last_occ = len(data[:-1]) - list(reversed(data[:-1])).index(data[-1]) -  1
		
		return len(data[:-1]) - last_occ

	else:

		return 0

input_data = '2,15,0,9,1,20'
#input_data = '0,3,6'
data = read_input_data(input_data)

new_number = 0

for y in range(2020):

	if y < len(data):
		new_number = data[y]

	else:

		new_number = find_next_number(data)
	
		data.append(new_number)

	print(f'{y+1} - {new_number}')