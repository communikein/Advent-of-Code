import itertools

input = open('nums.txt', 'r') 
tmp = input.readlines()

nums = []
for i in tmp:
	nums.append(int(i))

combs = list(itertools.combinations(nums, 3))

for comb in combs:
	if comb[0] + comb[1] + comb[2] == 2020:
		print(comb[0] * comb[1] * comb[2])