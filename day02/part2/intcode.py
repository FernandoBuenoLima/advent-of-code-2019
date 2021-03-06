
def get_data(program, position):
    return program[program[position]]

def perform_sum(program, position):
    program[program[position+3]] = get_data(program, position+1) + get_data(program, position+2)
    return program, (position + 4)
    
def perform_multiply(program, position):
    program[program[position+3]] = get_data(program, position+1) * get_data(program, position+2)
    return program, (position + 4)

def run(program, noun, verb):
    program[1] = noun
    program[2] = verb
    
    position = 0
    opcode = program[position]
    
    while opcode != 99:
        if opcode == 1:
            program, position = perform_sum(program, position)
        elif opcode == 2:
            program, position = perform_multiply(program, position)
        else:
            print("something went wrong")
            return -1
        opcode = program[position]
        
    return program[0]

def find_inputs(program, goal):
    for noun in range(100):
        for verb in range(100):
            if run(program.copy(), noun, verb) == goal:
                return 100 * noun + verb

with open("input.txt") as file:
    a_str = file.read().split(',')
    program = []
    for c in a_str:
        program.append(int(c))

    print(find_inputs(program, 19690720))
