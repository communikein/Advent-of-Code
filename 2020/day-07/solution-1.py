import math

TARGET_BAG_COLOR = 'shiny gold'

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def format_data(input_data):
	bags_rules = {}
	
	for bag_rule in input_data:
		container_bag_type = bag_rule.split(' bags contain ')[0]
		contained_bags_type = bag_rule.split(' bags contain ')[1]
		contained_bags_type = contained_bags_type.replace(' bags', '').replace(' bag', '')
		contained_bags_type = contained_bags_type.replace('.', '').split(', ')

		bags_rules[container_bag_type] = {}
		
		# If this bag can't contain any other bags, move on
		if len(contained_bags_type) == 1 and contained_bags_type[0] == 'no other':
			continue

		contained_bags = []
		for contained in contained_bags_type:
			number = contained.split(' ')[0]
			bag_type = ' '.join(contained.split(' ')[1:])

			bags_rules[container_bag_type][bag_type] = number

	return bags_rules


def create_tree(data, current_color, current_quantity, parent_color, tree):
	sub_tree = {
		'current_color': current_color,
		'current_quantity': current_quantity,
		'parent_color': parent_color,
		'children': []
		}
	tree['children'].append(sub_tree)

	# If the node has no child, exit recursion
	if not data[current_color]:
		return tree

	else:
		for child_color in data[current_color]:
			parent_color = current_color
			child_quantity = data[current_color][child_color]
			
			create_tree(data, child_color, int(child_quantity), parent_color, sub_tree)

	#return tree

def traverse_tree(tree, tree_count, result=[]):
	
	# Skip root
	if tree['current_color']:
		#print(tree_count, result)
		result.append(tree['current_color'])		

	# (Base case) 
	if tree['current_color'] == TARGET_BAG_COLOR:
		tree_count.extend(result)
		#print(tree_count, result)
		result.clear()

	# Recursive case
	else:
		if debug:
			print(f'{tree["current_color"]} -- bags: {result} -- subtree: {tree_count}')

		# If script reached the end of the subtree, reset counter
		if not tree['children']:
			#print('CLEARING LIST')
			result.clear()

		for child in tree['children']:
			if debug:
				print(f'{tree["current_color"]} -- bags: {result} -- subtree: {tree_count}')

			traverse_tree(child, tree_count, result)
			if TARGET_BAG_COLOR in tree_count:
				break


input_data = read_input_data('input.txt')
bag_rules = format_data(input_data)

global debug
debug = False

trees = []
total = 0
final = set()
for key, values in bag_rules.items():
	
	tree = {
		'current_color': None,
		'current_quantity': 0,
		'parent_color': None,
		'children': []
	}
	create_tree(bag_rules, key, 1, None, tree)

	bags_containing_shiny_gold = []
	traverse_tree(tree, bags_containing_shiny_gold)
	
	if len(bags_containing_shiny_gold) > 0:
		total += 1

print(f'bags: {total - 1}')
