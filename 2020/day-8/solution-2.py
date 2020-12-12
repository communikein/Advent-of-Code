CMD = 'cmd'
ARG = 'arg'

CMD_JMP = 'jmp'
CMD_ACC = 'acc'
CMD_NOP = 'nop'

def read_input_data(file):
	with open(file, 'r') as input_file:
		result = input_file.read().split('\n')

	return result

def format_data(input_data):
	instructions = []
	
	for line in input_data:
		cmd = line.split(' ')[0]
		arg = int(line.split(' ')[1])

		instructions.append({CMD: cmd, ARG: arg})

	return instructions


acc = 0
input_data = read_input_data('input.txt')
instructions = format_data(input_data)

instr_pointer = 0
pointer_history = []
target_pointer = len(instructions)

changed = False
last_instr_pointer = 0
last_acc = 0
edited_pointers = []
edited_history = []


while instr_pointer < len(instructions):
	
	if instr_pointer in pointer_history or instr_pointer in edited_history:
		print(f'WRONG SWAP, REVERTING')

		instr_pointer = last_instr_pointer 
		edited_history = []
		acc = last_acc
		changed = False

	if instr_pointer == target_pointer:
		print(f'\n\nACC final is: {acc}')
		break		

	instr = instructions[instr_pointer]

	if instr[CMD] == CMD_ACC:
		acc += instr[ARG]

		if changed:
			edited_history.append(instr_pointer)
		else:
			pointer_history.append(instr_pointer)

		print(f'{instr_pointer+1} \t ACC {instr[ARG]}')
		instr_pointer += 1

	elif instr[CMD] == CMD_JMP:
		
		# Changed the command before, don't change it again
		if instr_pointer in edited_pointers:
			pointer_history.append(instr_pointer)

			print(f'{instr_pointer+1} \t JMP {instr[ARG]}')
			instr_pointer += instr[ARG]
		
		# Didn't change this command before
		else:

			# Already changed another command, don't change this one
			if changed:
				edited_history.append(instr_pointer)

				print(f'{instr_pointer+1} \t JMP {instr[ARG]}')
				instr_pointer += instr[ARG]
			
			# Didn't change any other command, change this one
			else:
				changed = True
				last_instr_pointer = instr_pointer
				last_acc = acc
				edited_pointers.append(instr_pointer)

				print(f'{instr_pointer+1} \t CHANGED JMP {instr[ARG]} to NOP {instr[ARG]}')
				instr_pointer += 1
	
	# If instruction is NOP
	else:

		# Changed the command before, don't change it again
		if instr_pointer in edited_pointers:
			pointer_history.append(instr_pointer)

			print(f'{instr_pointer+1} \t NOP {instr[ARG]}')
			instr_pointer += 1

		# Didn't change this command before
		else:

			# Already changed another command, don't change this one
			if changed:
				edited_history.append(instr_pointer)

				print(f'{instr_pointer+1} \t NOP {instr[ARG]}')
				instr_pointer += 1

			# Didn't change any other command, change this one
			else:
				changed = True
				last_instr_pointer = instr_pointer
				last_acc = acc
				edited_pointers.append(instr_pointer)

				print(f'{instr_pointer+1} \t CHANGED NOP {instr[ARG]} to JMP {instr[ARG]}')
				instr_pointer += instr[ARG]

print(f'\n\nACC final is: {acc}')