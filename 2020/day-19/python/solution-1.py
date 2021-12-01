import re
import itertools

FORK = '|'
RULE = ':'


rules_rule = '((?:\w+)|(?:\|))'

def read_input_data(file):
	with open(file, 'r') as input_file:
		temp = input_file.read().split('\n\n')

	rules_raw = temp[0].split('\n')
	data_raw = temp[1].split('\n')

	rules_step = sorted([re.findall(rules_rule, line) for line in rules_raw])
	rules = {i: rule[1:] for i, rule in enumerate(rules_step)}

	return {'rules': rules, 'data': data_raw}

def _split_rule_forks(rule):

	fork = []

	index = 0
	for el in rule:
		
		if el == FORK:
			fork.append([int(e) if e.isdigit() else e for e in rule[0:index]])
			fork.append([int(e) if e.isdigit() else e for e in rule[index+1:]])

		index += 1

	if not fork:
		if len(rule) == 1 and type(rule[0]) is str:
			fork = rule[0]
		else:
			fork = [int(e) if e.isdigit() else e for e in rule]

	return fork

def split_rules_forks(rules):
	
	result = {}

	for rule in rules:

		new_rule = _split_rule_forks(rules[rule])
		result[rule] = new_rule

	return result


def _explore_rule(rules, rule, recursion_depth=0):

	if not type(rule) is str:
		print(f'{" "*recursion_depth*4}Analysing rule: {rule}')

	result = []

	# Analyse all the referenced rules
	for el in rule:

		# If the current element does not reference another rule
		if type(el) is str:

			print(f'{" "*recursion_depth*4}Found value {el}')
			ref_rule = el
		
		# If the current element references another rule, explore that rule
		elif type(el) is int:
			
			print(f'{" "*recursion_depth*4}Fetching rule {el}')
			ref_rule = _explore_rule(rules, rules[el], recursion_depth+1)

		# If the current element is a list of rules, explore them
		else:

			print(f'{" "*recursion_depth*4}Fetching rules {el}')
			ref_rule = _explore_rule(rules, el, recursion_depth+1)
		
		result.extend(ref_rule)

	if len(result) == 1 and type(result[0]) is str:
		result = ''.join(result)

	print(f'{" "*recursion_depth*4}Step result: {result}')
	# If all elements in result are strings, join them together
	final = join_combine_rules(result, recursion_depth)

	print(f'{" "*recursion_depth*4}Result: {final}\n')

	return final

def join_combine_rules(rules, recursion_depth):

	if len(rules) == 1:

		print(f'{" "*recursion_depth*4}Concatenating lists')
		return rules[0]


	if len(rules) % 2 == 0:

		# If the list contains lists
		#if any([type(el) is list for el in rules]):
		print(f'{" "*recursion_depth*4}Combining lists --- {len(rules) % 2}')

		result = [el + el2 for el in rules[0] for el2 in rules[1]]
		return result


	print(f'{" "*recursion_depth*4}BOH --- {len(rules) % 2}')
	return [''.join(rules)]

	'''
	if type(rules) is str:
		print(f'{" "*recursion_depth*4}Joining lists')
		return "".join(rules)
	'''

	'''
	# If all elements in result are strings, join them together
	if not type(rules) is int and len(rules) <= 2 and all([(type(el) == str and len(el) <2) for el in rules]):
		print(f'{" "*recursion_depth*4}Joining lists')
		return "".join(rules)
	'''
	print(f'{" "*recursion_depth*4}BOH')
	return rules



def expand_rule(rule, all_rules):

	result = None

	for el in rule:

		if type(el) is list:

			step_result = expand_rule(el, all_rules)
			
			if type(result) is list:
				result.append(step_result)
			
			else:

				if result == None:
					result = []

				result.append(step_result)

		elif type(el) is int:

			step_result = expand_rule(all_rules[el], all_rules)

			if type(result) is list:
				result.append(step_result)
			
			else:

				if result == None:
					result = []

				result.append(step_result)

		else:

			step_result = el

			if type(result) is list:
				result.extend(step_result)
			
			else:
				result = step_result

	return result

def compute_rule(rule, tabs=0, result=[]):
	
	print(f'{" "*tabs*4}rule: {rule}')

	temp = []

	for el in rule:

		if type(el) is list:

			temp.append(compute_rule(el, tabs+1))

			'''
			print(f'{" "*(tabs+1)*4}prova: {prova}')
			temp.append(add_elements_in_order(prova))
			print(f'{" "*(tabs+1)*4}prova: {temp}')
			'''

		else:
			temp.append(el)
			print(f'{" "*(tabs+1)*4}el: {el}')

	print(f'{" "*(tabs)*4}prova: {temp}')

	if not all([type(el) is str for el in temp]):
		
		print(f'{" "*(tabs)*4}concatenate')
		temp = [el[0] for el in temp]
	else:
		print(f'{" "*(tabs)*4}combine')
		temp = add_elements_in_order(temp)
	print(f'{" "*(tabs)*4}temp: {temp}')

	return temp

def add_elements_in_order(rule):
	
	# If both are lists
	if all([type(el) is list for el in rule]):

		# If at least one list has more than one element,
		# combine the two lists: 1st of 1st with 1st of 2nd, 1st of 1st with 2nd of 2nd
		if any([len(el) > 1 for el in rule]):
			result = [el + el2 for el in rule[0] for el2 in rule[1]]

		# Return the two lists joined
		else:
			result = rule[0] + rule[1]

	# If only one is a list
	elif any([type(el) is list for el in rule]):

		# And if that list has more than 1 element
		if any([len(el) > 1 for el in rule]):
			result = [el + el2 for el in rule[0] for el2 in rule[1]]

		# Return the two lists joined
		else:
			result = rule[0] + rule[1]

	# If they are all strings
	else:

		result = [''.join(rule)]

	return result

def compute_rule_v2(rule, tabs=0, result=[]):
	
	print(f'{" "*tabs*4}rule: {rule}')

	temp = []

	for el in rule:

		if type(el) is list:
			temp.append(compute_rule_v2(el, tabs+1))

		else:
			temp.append(el)
			print(f'{" "*(tabs+1)*4}el: {el}')

	print(f'{" "*(tabs)*4}temp before: {temp}')
	#
	temp_2 = add_elements_in_order(temp)
	#
	print(f'{" "*(tabs)*4}temp after:  {temp_2}')

	return temp_2

new_data = read_input_data('../input.txt')
rules = split_rules_forks(new_data['rules'])
print(rules)

rule_expanded = expand_rule(rules[0], rules)
print(rule_expanded)

res = compute_rule_v2(rule_expanded)
print('\n\n\n\n\n', res)

'''
print()
for el in rule_expanded:
	print(el)
'''