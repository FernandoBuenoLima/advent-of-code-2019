
#accessMode
#   0 - position mode
#   1 - immediate mode
def get_data(program, address, accessMode):
    if accessMode == 0:
        return program[program[address]]
    elif accessMode == 1:
        return program[address]
            
    print("get_data() exception - unrecognized accessMode: " + accessMode)
    return "error"

def perform_sum(program, address, parameterAccessModes):
    program[program[address+3]] = get_data(program, address+1, parameterAccessModes[0]) + get_data(program, address+2, parameterAccessModes[1])
    return program, (address + 4)
    
def perform_multiply(program, address, parameterAccessModes):
    program[program[address+3]] = get_data(program, address+1, parameterAccessModes[0]) * get_data(program, address+2, parameterAccessModes[1])
    return program, (address + 4)

def perform_input(program, address):
    program[program[address+1]] = int(input("input > "))
    return program, (address + 2)

def perform_output(program, address, parameterAccessModes):
    print(get_data(program, address+1, parameterAccessModes[0]))
    return program, (address + 2)

def parse_instruction(instruction):
    s_instr = str(instruction)
    
    if len(s_instr) == 1:
        return int(s_instr[-1:]), [0, 0, 0]
        
    opcode = int(s_instr[-2:])
    parameterAccessModes = [0, 0, 0]
    parameterPosition = 0
    
    for i in range(len(s_instr) - 3, -1, -1):
        parameterAccessModes[parameterPosition] = int(s_instr[i])
        parameterPosition += 1
    
    return opcode, parameterAccessModes

def run(program):
    instruction_pointer = 0
    opcode, parameterAccessModes = parse_instruction(program[instruction_pointer])
    
    while opcode != 99:
        if opcode == 1:
            program, instruction_pointer = perform_sum(program, instruction_pointer, parameterAccessModes)
        elif opcode == 2:
            program, instruction_pointer = perform_multiply(program, instruction_pointer, parameterAccessModes)
        elif opcode == 3:
            program, instruction_pointer = perform_input(program, instruction_pointer)
        elif opcode == 4:
            program, instruction_pointer = perform_output(program, instruction_pointer, parameterAccessModes)
        else:
            print("run() exception - unrecognized opcode: " + str(opcode))
            return program, opcode
        opcode, parameterAccessModes = parse_instruction(program[instruction_pointer])
        
    return program, opcode

