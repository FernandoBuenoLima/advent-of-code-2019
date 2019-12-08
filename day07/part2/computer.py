from intcode import *

def runThrusters(program, phaseInputs):
    thrusters = []
    signal = 0
    outSignal = 0
    
    for i in range(5):
        computer = IntcodeComputer(program)
        signal = computer.run([phaseInputs[i], signal])
        thrusters.append(computer)
    
    while outSignal is not None:
        for i in range(5):
            outSignal = thrusters[i].run([signal])
            if outSignal is None:
                break
            signal = outSignal
            
    return signal


program = []

with open("input.txt") as file:
    a_str = file.read().split(',')
    for c in a_str:
        program.append(int(c))

maxSignal = -1

for i in range(5,10):
    for j in range(5,10):
        if j != i:
            for k in range(5,10):
                if k not in [i, j]:
                    for l in range(5,10):
                        if l not in [i, j, k]:
                            for m in range(5,10):
                                if m not in [i, j, k, l]:
                                    signal = runThrusters(program, [i, j, k, l, m])
                                    maxSignal = signal if signal > maxSignal else maxSignal

print(maxSignal)
