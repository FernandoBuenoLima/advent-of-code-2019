from intcode import *

program = []

with open("input.txt") as file:
    a_str = file.read().split(',')
    for c in a_str:
        program.append(int(c))

result, exit_code = run(program)

print("\n\n\n\n")
print(result)
print("\n\n")
print("program ended with exit code: " + str(exit_code))
