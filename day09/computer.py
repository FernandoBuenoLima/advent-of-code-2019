from intcode import *

program = []

with open("input.txt") as file:
    a_str = file.read().split(',')
    for c in a_str:
        program.append(int(c))

computer = IntcodeComputer(program)
computer.run()

exit()
