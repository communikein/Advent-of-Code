import itertools

input_file = open('input.txt', 'r') 
input_data = input_file.readlines()

rules = [] 
cont = 0
for i in input_data:
	tmp = i.split(" ")
	rule = {
		'pos1': int(tmp[0].split("-")[0]),
		'pos2': int(tmp[0].split("-")[1]),
		'chr': tmp[1][:-1],
		'pwd': tmp[2].strip(),
	}

	rules.append(rule)

	print(rule)
	if (rule['chr'] in rule['pwd']) and (rule['pwd'][rule['pos1']-1] == rule['chr']):
		if rule['pwd'][rule['pos1']-1] != rule['pwd'][rule['pos2']-1]:
			cont += 1
	if (rule['chr'] in rule['pwd']) and (rule['pwd'][rule['pos2']-1] == rule['chr']):
		if rule['pwd'][rule['pos1']-1] != rule['pwd'][rule['pos2']-1]:
			cont += 1

print(cont)