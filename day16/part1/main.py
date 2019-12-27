base_pattern = [0, 1, 0, -1]

def applyPhase(input):
    output = []
    
    for i in range(len(input)):
        pattern = []
        for n in base_pattern:
            pattern.extend([n] * (i+1))
        
        pIndex = 1
        total = 0
        for n in input:
            total += (n * pattern[pIndex])
            pIndex = (pIndex + 1) % len(pattern)
        output.append(abs(total) % 10)
    
    return output

input = [int(c) for c in open("input.txt").read()]

output = input.copy()
for i in range(100):
    output = applyPhase(output)

s = ""
for i in range(8):
    s += str(output[i])
print(s)