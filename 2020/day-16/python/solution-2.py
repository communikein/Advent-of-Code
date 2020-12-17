import re
from datetime import datetime 
import math

tickets_rules_re ='(?:([a-z ]+): ([\d-]+) or ([\w-]+))'
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

def is_num_valid(num, rules):
	
	valid_rules = set()

	for rule in rules:

		if debug:
			print(f'Analyzing {num} against rule {rule_ranges}')

		for ranges in rules[rule]:

			if num >= ranges['min'] and num <= ranges['max']:
				if debug:
					print(f'Num in range.')

				valid_rules.add(list(rules.keys()).index(rule))

	return len(valid_rules) > 0, valid_rules

def is_ticket_valid(rules, ticket):
	valid = True
	non_valid_nums = []
	result = {}

	for num in ticket:

		result[ticket.index(num)] = []

		if debug:
			print(f'Analyzing number {num}')

		validity, valid_rules = is_num_valid(num, rules)
		result[ticket.index(num)] = valid_rules

		if not validity:
			valid = False

	return valid, result

def get_valid_tickets(rules, tickets):
	
	nums_rules = []
	to_remove = []
	index = 0
	for ticket in tickets:
		
		ticket_valid, num_rule = is_ticket_valid(rules, ticket)
		
		if not ticket_valid:
			to_remove.append(index)
		else:
			nums_rules.append(num_rule)

		index += 1

	index = 0
	for remove in to_remove:
		del tickets[remove-index]
		index += 1

	return [{'ticket': tickets[i], 'num_rule': nums_rules[i]} for i in range(len(tickets))]

global debug
debug = False

data = read_input_data('../input.txt')
if debug:
	print(data)

rules = data['tickets_rules']
tickets = data['my_ticket'] + data['other_tickets']
valid_tickets = get_valid_tickets(rules, tickets)


result = [set() for _ in range(len(valid_tickets[0]['num_rule']))]

#print(valid_tickets[0])
print()

for num in valid_tickets[0]['num_rule']:
	result[num].update(valid_tickets[0]['num_rule'][num])
	#print(result[num])

print()
for valid_ticket in valid_tickets:
	#print(f'\nTicket - {valid_ticket["ticket"]}')
	for num in valid_ticket['num_rule']:
		result[num] = set.intersection(result[num], valid_ticket['num_rule'][num])
		#print(num, result[num])

index = 0

for d in range(20):
	for index in range(len(result)):

		if len(result[index]) == 1:

			for m in range(index+1,len(result)):
				result[m].discard(list(result[index])[0])

			for m in range(0, index):
				result[m].discard(list(result[index])[0])

print()
cont = 0
temp = {}
for x in result:
	temp[list(x)[0]] = cont
	cont += 1


result = [temp[x] for x in sorted(temp)]

print(result[:6])

final = [valid_tickets[0]['ticket'][index] for index in result[:6]]
print(final)
print(math.prod(final))

'''
for index in range(6):
	if index in result:
		print(valid_tickets[0]['ticket'][index])
'''