from string import *

def run(program: list):
	line = 0
	full = len(program)
	variables = initialise_variables()
	locations = populate_locations(program)
	printable = list()
	while line < full:
		instruction = program[line]
		if instruction.startswith("PRINT"):
			printable.append(execute_print(instruction, variables))
		elif instruction.startswith("MOV"):
			execute_mov(instruction, variables)
		elif instruction.startswith("ADD"):
			execute_add(instruction, variables)
		elif instruction.startswith("SUB"):
			execute_sub(instruction, variables)
		elif instruction.startswith("MUL"):
			execute_mul(instruction, variables)
		elif instruction.startswith("JUMP"):
			line = execute_jump(instruction, locations)
			continue
		elif instruction.startswith("IF"):
			evaluation = execute_if(instruction, variables) # Evaluates if the condition is true
			if evaluation[0]:
				line = execute_jump(evaluation[1], locations) # If true, executes the jump
				continue
		elif instruction.startswith("END"):
			return printable
		else:
			pass
		line += 1
	return printable

def initialise_variables():
	variables = dict()
	for i in range(65, 91): # Assigns a letter in the Latin alphabet to each variable according to their ASCII value
		variables[chr(i)] = 0
	return variables

def populate_locations(program: list):
	locations = dict()
	line = 0
	for instruction in program:
		if instruction.endswith(":"):
			locations[instruction[:-1]] = line # Removes the ":" at the end of the location name
		line += 1
	return locations

def execute_print(instruction: str, variables: dict):
	tokens = instruction.split()
	if tokens[1] in ascii_letters:
		return variables[tokens[1]]
	else:
		return int(tokens[1])

def execute_mov(instruction: str, variables: dict):
	tokens = instruction.split()
	if tokens[2] in ascii_letters:
		variables[tokens[1]] = variables[tokens[2]]
	else:
		variables[tokens[1]] = int(tokens[2])

def execute_add(instruction: str, variables: dict):
	tokens = instruction.split()
	if tokens[2] in ascii_letters:
		variables[tokens[1]] = variables[tokens[1]] + variables[tokens[2]]
	else:
		variables[tokens[1]] = variables[tokens[1]] + int(tokens[2])

def execute_sub(instruction: str, variables: dict):
	tokens = instruction.split()
	if tokens[2] in ascii_letters:
		variables[tokens[1]] = variables[tokens[1]] - variables[tokens[2]]
	else:
		variables[tokens[1]] = variables[tokens[1]] - int(tokens[2])

def execute_mul(instruction: str, variables: dict):
	tokens = instruction.split()
	if tokens[2] in ascii_letters:
		variables[tokens[1]] = variables[tokens[1]] * variables[tokens[2]]
	else:
		variables[tokens[1]] = variables[tokens[1]] * int(tokens[2])

def execute_jump(instruction: str, locations: dict):
	tokens = instruction.split()
	target_line = tokens[1]
	if target_line in locations:
		return locations[target_line]
	return -1

def execute_if(instruction: str, variables: dict):
	tokens = instruction.split()
	first_var = tokens[1]
	operator = tokens[2]
	second_var = tokens[3]
	location = tokens[5]
	if first_var in ascii_letters:
		first_var = variables[first_var]
	else:
		first_var = int(first_var)
	if second_var in ascii_letters:
		second_var = variables[second_var]
	else:
		second_var = int(second_var)
	if operator == ">":
		return (first_var > second_var, f"JUMP {location}")
	elif operator == ">=":
		return (first_var >= second_var, f"JUMP {location}")
	elif operator == "<":
		return (first_var < second_var, f"JUMP {location}")
	elif operator == "<=":
		return (first_var <= second_var, f"JUMP {location}")
	elif operator == "!=":
		return (first_var != second_var, f"JUMP {location}")
	else:
		return (first_var == second_var, f"JUMP {location}")

if __name__ == "__main__":
	program1 = []
	program1.append("MOV A 1")
	program1.append("MOV B 2")
	program1.append("PRINT A")
	program1.append("PRINT B")
	program1.append("ADD A B")
	program1.append("PRINT A")
	program1.append("END")
	result = run(program1)
	print(result)
	program2 = []
	program2.append("MOV A 1")
	program2.append("MOV B 10")
	program2.append("begin:")
	program2.append("IF A >= B JUMP quit")
	program2.append("PRINT A")
	program2.append("PRINT B")
	program2.append("ADD A 1")
	program2.append("SUB B 1")
	program2.append("JUMP begin")
	program2.append("quit:")
	program2.append("END")
	result = run(program2)
	print(result)
	program3 = []
	program3.append("MOV A 1")
	program3.append("MOV B 1")
	program3.append("begin:")
	program3.append("PRINT A")
	program3.append("ADD B 1")
	program3.append("MUL A B")
	program3.append("IF B <= 10 JUMP begin")
	program3.append("END")
	result = run(program3)
	print(result)
	program4 = []
	program4.append("MOV N 50")
	program4.append("PRINT 2")
	program4.append("MOV A 3")
	program4.append("begin:")
	program4.append("MOV B 2")
	program4.append("MOV Z 0")
	program4.append("test:")
	program4.append("MOV C B")
	program4.append("new:")
	program4.append("IF C == A JUMP error")
	program4.append("IF C > A JUMP over")
	program4.append("ADD C B")
	program4.append("JUMP new")
	program4.append("error:")
	program4.append("MOV Z 1")
	program4.append("JUMP over2")
	program4.append("over:")
	program4.append("ADD B 1")
	program4.append("IF B < A JUMP test")
	program4.append("over2:")
	program4.append("IF Z == 1 JUMP over3")
	program4.append("PRINT A")
	program4.append("over3:")
	program4.append("ADD A 1")
	program4.append("IF A <= N JUMP begin")
	result = run(program4)
	print(result)
	program5 = []
	program5.append("MOV A 1")
	program5.append("MOV B 1")
	program5.append("start:")
	program5.append("MUL A 2")
	program5.append("ADD B 1")
	program5.append("IF B != 101 JUMP start")
	program5.append("PRINT A")
	result = run(program5)
	print(result)