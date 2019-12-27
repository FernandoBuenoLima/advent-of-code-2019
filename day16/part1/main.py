base_pattern = [0, 1, 0, -1]

def applyPhase(input):
    output = []
    inputSize = len(input)
    
    for i in range(inputSize):
        total = 0
        
        j = i
        multiplier = 1
        while j < inputSize:
            for k in range(j, j+i+1):
                if k >= inputSize:
                    break
                total += input[k] * multiplier
            j += (2 * i) + 2
            multiplier *= -1
        
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
