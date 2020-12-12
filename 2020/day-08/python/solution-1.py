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
input_data = read_input_data('../input.txt')
instructions = format_data(input_data)

cont = 0
instr_pointer = 0
pointer_history = []
while instr_pointer < len(instructions):
	instr = instructions[instr_pointer]
	
	if instr_pointer in pointer_history:
		print(f'\n\nACC final is: {acc}')
		break

	if instr[CMD] == CMD_ACC:
		acc += instr[ARG]
		pointer_history.append(instr_pointer)
		print(f'{instr_pointer+1} \t ACC {instr[ARG]}')
		instr_pointer += 1
		
	elif instr[CMD] == CMD_JMP:
		pointer_history.append(instr_pointer)
		print(f'{instr_pointer+1} \t JMP {instr[ARG]}')
		instr_pointer += instr[ARG]
		
	else:
		print(f'{instr_pointer+1} \t NOP {instr[ARG]}')
		pointer_history.append(instr_pointer)
		instr_pointer += 1
		continue

	cont += 1
