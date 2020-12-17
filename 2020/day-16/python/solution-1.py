import re
from datetime import datetime 

tickets_rules_re ='(?:(\w+): ([\d-]+) or ([\w-]+))'
ticket_numbers_re = '((?:\d,?)+)\n?'

starting_time = datetime.now()

def read_input_data(file):
	with open(file, 'r') as input_file:
		temp = input_file.read().split('\n\n')

	# Gather tickets rules
	ticket_rules_matches = re.findall(tickets_rules_re, temp[0])
	rules = {rule[0]: [{'min': int(ranges.split('-')[0]), 'max': int(ranges.split('-')[1])} for ranges in rule[1:]] for rule in ticket_rules_matches}
	
	# Gather nearby tickets numbers
	others_ticket_numbers_matches = re.findall(ticket_numbers_re, temp[2])
	other_tickets = [list(map(int, ticket.split(','))) for ticket in others_ticket_numbers_matches]

	# Gather my ticket numbers
	my_ticket_numbers_matches = re.findall(ticket_numbers_re, temp[1])[0]
	my_ticket = [list(map(int, my_ticket_numbers_matches.split(',')))]
	
	return {'tickets_rules': rules, 'my_ticket': my_ticket, 'other_tickets': other_tickets}

def is_ticket_valid(rules, ticket):
	valid = True
	non_valid_num = None

	for num in ticket:

		if debug:
			print(f'Analyzing number {num}')

		for rule in rules:
			rule_valid = False

			if debug:
				print(f'Analyzing rule {rules[rule]} --- {valid}')

			for ranges in rules[rule]:

				if num >= ranges['min'] and num <= ranges['max']:
					if debug:
						print(f'Number {num} in range {ranges}')

					rule_valid = True
					break

			if rule_valid:
				break

		valid = valid and rule_valid

		if not valid:
			non_valid_num = num
			break

	return non_valid_num


global debug
debug = True

data = read_input_data('../input.txt')
#if debug:
	#print(data)

total = []
for ticket in data['other_tickets']:
	print('\n', ticket)
	
	non_valid_num = is_ticket_valid(data['tickets_rules'], ticket)
	print(non_valid_num)

	if non_valid_num != None:
		total.append(non_valid_num)

print(sum(total))