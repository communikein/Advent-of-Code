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

def traverse_tree(tree, total=0):
	
	# If this is the last node of the subtree
	if not tree['children'] or len(tree['children']) == 0:
		if debug:
			print(f'{tree["current_color"]} -- quantity: {tree["current_quantity"]}')
		return tree['current_quantity']

	# If node has children
	else:
		sum_children = 0
		
		if debug:
			print(f'{tree["current_color"]} -- sum_children: {sum_children}')
			print(f'Found {len(tree["children"])} children')

		for child in tree['children']:
			if debug:
				print(f'Analysing child {child["current_color"]} -- parent: {child["parent_color"]}')

			temp = traverse_tree(child, total)
			sum_children += temp

		if tree['parent_color'] != None:
			subtree_total = tree['current_quantity'] + tree['current_quantity'] * sum_children
			if debug:
				print(f'{tree["current_color"]} -- subtree_total: {subtree_total} -- sum_children: {sum_children}\n')

			return subtree_total

		return sum_children


input_data = read_input_data('input.txt')
bag_rules = format_data(input_data)

global debug
debug = False

tree = {
	'current_color': None,
	'current_quantity': 0,
	'parent_color': None,
	'children': []
}

create_tree(bag_rules, TARGET_BAG_COLOR, 1, None, tree)

result = traverse_tree(tree)
print(f'bags: {result}')
