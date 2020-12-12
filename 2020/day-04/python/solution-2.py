import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

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
		
		if not all(required in passport.keys() for required in required_fields):
			continue

		if not (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2020):
			continue

		if not (int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
			continue

		if not (int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
			continue

		if not (passport['hgt'][-2:] == 'cm' and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193):
			if not (passport['hgt'][-2:] == 'in' and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76):
				continue

		if not (len(passport['hcl']) == 7 and re.search("[a-z0-9]{6}", passport['hcl'])):
			continue

		if not (passport['ecl'] in valid_eye_color):
			continue

		if not (len(passport['pid']) == 9):
			continue

		result.append(passport)

	return result

input_data = read_input_data('../input.txt')
fixed_data = format_input_data(input_data)
valid_passports = check_passports(fixed_data)
print(len(valid_passports))