from intcode import IntcodeComputer
from lib import *

computer = IntcodeComputer(open("input.txt").read())

image = []
line = []
output = computer.run()
while output is not None:
    if output == 10:
        image.append(line.copy())
        line = []
    else:
        line.append(chr(output))
    output = computer.run()

width = len(image[0])
height = len(image)

scaffChars = ['#', '>', '<', '^', 'v']

total = 0

for y in range(1, height-2):
    for x in range(1, width-2):
        if image[y][x] in scaffChars:
            if image[y-1][x] in scaffChars:
                if image[y][x-1] in scaffChars:
                    if image[y+1][x] in scaffChars:
                        if image[y][x+1] in scaffChars:
                            total += x * y

print(total)