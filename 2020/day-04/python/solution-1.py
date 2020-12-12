import itertools
import math

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def read_input_data(file):
	input_file = open(file, 'r') 
	input_data = input_file.readlines()
	
	result = []
	for line in input_data:
		line = line.strip()
		result.append(line)

	return result

def format_input_data(input_data):
	single = {}
	result = []
	for line in input_data:
		if line != '':
			fields_raw = line.split(' ')
			for field in fields_raw:
				single[field.split(':')[0]] = field.split(':')[1]
		else:
			result.append(single)
			single = {}
			continue

	return result

def check_passports(passports):
	result = []
	for passport in passports:
		if all(required in passport.keys() for required in required_fields):
			result.append(passport)

	return result

input_data = read_input_data('../input.txt')
fixed_data = format_input_data(input_data)
valid_passports = check_passports(fixed_data)
print(len(valid_passports))