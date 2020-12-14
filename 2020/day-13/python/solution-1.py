import math
import re


def read_input_data(file):
	with open(file, 'r') as input_file:
		temp = input_file.read()

	result = temp.replace('x,', '').replace(',x', '').replace('\n', ' ').replace(',', ' ').split()
	
	return result


global debug
debug = True

input_data = read_input_data('input.txt')

min_time = input_data[0]
bus_rtt = input_data[1:]

waiting_times = []
for bus in bus_rtt:

	current = int(bus) - (int(min_time) % int(bus))

	waiting_times.append(current)

min_wait = min(waiting_times)
index = int(bus_rtt[waiting_times.index(min_wait)])

result = min_wait * index
print(result)