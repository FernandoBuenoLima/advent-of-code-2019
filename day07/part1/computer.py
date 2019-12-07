from intcode import *

def runThrusters(program, phaseInputs):
    currentSignal = 0
    
    for i in range(5):
        currentProgram = program.copy()
        currentProgram, opcode, currentSignal = run(currentProgram, [phaseInputs[i], currentSignal])
    
    return currentSignal

program = []

with open("input.txt") as file:
    a_str = file.read().split(',')
    for c in a_str:
        program.append(int(c))

maxSignal = -1

for i in range(5):
    for j in range(5):
        if j != i:
            for k in range(5):
                if k not in [i, j]:
                    for l in range(5):
                        if l not in [i, j, k]:
                            for m in range(5):
                                if m not in [i, j, k, l]:
                                    signal = runThrusters(program, [i, j, k, l, m])
                                    maxSignal = signal if signal > maxSignal else maxSignal

print("\n\n\n")
print(maxSignal)
